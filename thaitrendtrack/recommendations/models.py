from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences = models.JSONField(default=list)
    history = models.JSONField(default=list)
    is_first_login = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


from django.db import models
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np
import pickle
import json

# ✅ โหลดโมเดล
tokenizer = AutoTokenizer.from_pretrained("MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
model = AutoModel.from_pretrained("MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
model.eval()

def get_embedding(text):
    """แปลงข้อความเป็นเวกเตอร์ embedding"""
    if not text or text.strip() == "":
        return np.zeros((1, 768)).tolist()

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].squeeze(0).numpy().tolist()


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title_th = models.CharField(max_length=255, blank=True, null=True)
    title_en = models.CharField(max_length=255, blank=True, null=True)
    original_title = models.CharField(max_length=255, blank=True, null=True)
    genres = models.JSONField(default=list)
    overview = models.TextField(blank=True, null=True)  # ✅ ใช้ overview
    status = models.CharField(max_length=100, blank=True, null=True)
    release_date = models.DateField(null=True, blank=True)
    poster_path = models.URLField(blank=True, null=True)
    cast = models.JSONField(default=list)
    watch_platforms = models.JSONField(default=dict)
    content_type = models.CharField(
        max_length=50, choices=[("Movie", "Movie"), ("TV Series", "TV Series")]
    )
    popularity = models.FloatField(blank=True, null=True)
    vote_average = models.FloatField(blank=True, null=True)
    runtime = models.CharField(max_length=50, blank=True, null=True)
    embedding = models.BinaryField(blank=True, null=True)  # ✅ เก็บ embedding ในแบบ pickle

    def save(self, *args, **kwargs):
        """สร้าง embeddings โดยใช้ overview เป็นหลัก"""
        if not self.embedding:
            genre_text = " ".join(self.genres)
            cast_text = " ".join(self.cast) if isinstance(self.cast, list) else ""
            platform_text = ", ".join([
                f"{country}: {', '.join(data.get('streaming', ['N/A']))}"
                for country, data in self.watch_platforms.items()
            ])

            combined_text = f"{self.overview} {genre_text} {cast_text} {platform_text} {self.content_type} {self.status}"
            print(f"🔄 Generating embedding for: {self.title_en}")

            embedding_vector = get_embedding(combined_text)
            self.embedding = pickle.dumps(embedding_vector)  # ✅ บันทึกเป็น binary

        super().save(*args, **kwargs)

    def get_embedding(self):
        """โหลด embedding กลับมาเป็น numpy array"""
        return np.array(pickle.loads(self.embedding)) if self.embedding else np.zeros(768)

    def __str__(self):
        return f"{self.title_th} ({self.title_en})"

# ThaiTrendTrack

ThaiTrendTrack is a dynamic platform designed to bridge the gap for international viewers by providing easy access to Thai entertainment content. Through personalized recommendations, robust translation features, and an engaging community, the platform makes Thai movies, series, and drama shows accessible and enjoyable for a global audience.

## Table of Contents
- [Background](#background)
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Background

Thai entertainment, encompassing movies, series, and drama shows, has emerged as a cultural phenomenon that transcends borders, captivating audiences not only within Thailand but also around the world. Renowned for its unique storytelling, compelling characters, and cultural richness, Thai entertainment has garnered considerable fame internationally. This popularity is evidenced by the growing fan base of enthusiasts who are drawn to the intricacies of Thai cinema and television.

The Thai government recognizes the significant economic and cultural value of its entertainment industry. Showcasing Thai entertainment on a global scale serves as a strategic initiative to promote Thai culture, heritage, and values to international audiences. By highlighting the diversity and creativity of Thai content, the government aims to bolster Thailand's global image and strengthen its soft power influence. Additionally, promoting Thai entertainment abroad contributes to the growth of the domestic entertainment industry, attracting investments, fostering talent development, and creating job opportunities within the sector.

## Problem Statement

Despite the widespread popularity of Thai movies, series, and drama shows, international viewers often face significant challenges in accessing this content due to language barriers. These limitations hinder the ability of enthusiasts to fully immerse themselves in the rich and diverse offerings of Thai entertainment, leading to frustration and a less satisfying viewing experience.

## Solution Overview

To overcome these accessibility challenges, ThaiTrendTrack proposes a comprehensive solution that enhances the viewing experience for global audiences. The platform is engineered to eliminate language barriers and deliver content that is both engaging and relevant to the user.

### Features

- **Personalized Recommendation System**  
  Utilizes user preferences to offer tailored content recommendations. The platform also provides a comprehensive catalog of Thai movies, series, and drama shows to ensure a diverse viewing experience.

- **Trending Recommendations**  
  Showcases popular titles based on the current interests and trends within the community.

- **For You Recommendations**  
  Offers a personalized selection of content that aligns with the unique tastes and preferences of each user.

- **Translation Button Feature**  
  Integrates a prominently displayed translation button in the user interface. This feature allows users to translate various textual elements—including titles, descriptions, and metadata—into their preferred language.

- **Community**  
  Fosters a vibrant space where users can connect, share recommendations, and discuss their favorite Thai entertainment content. This interactive community enhances user engagement and promotes a deeper appreciation of Thai culture.

## Getting Started

*Installation and setup instructions will be provided here.*

1. **Clone the Repository**
   ```bash
   https://github.com/ThaiTrendTrack/ThaiTrendTrack.git
    ```

2. **Install Dependencies**
   ```bash
    pip install -r requirements.txt
    ```
   
3. **Make Migration and Migrate**
   ```bash
    python manage.py makemigrations
    ```
   ```bash
    python manage.py migrate
    ```
   
4. **Upload databased**
   ```bash
    python manage.py import_movies
    ```
   ```bash
    python manage.py  get_embedding
    ```
    ```bash
    python manage.py insert_communities
    ```

5. **Run Server**
    ```bash
    python manage.py runserver
   ```
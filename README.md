# Système de Reconnaissance Faciale (Python)

## 📌 Présentation du projet
Ce projet implémente un **système de reconnaissance faciale basique** en Python. Il détecte les visages à partir d'un flux webcam et identifie les individus en les comparant avec une base de données locale.

Applications possibles :
- Systèmes de sécurité  
- Contrôle d’accès  
- Suivi de présence  
- Surveillance vidéo  

---

## ❓ Problématique
Comment concevoir un système capable de :
- Détecter les visages en temps réel  
- Identifier les personnes à partir d’une base de données  
- Afficher leurs informations si elles existent  
- Indiquer quand une personne est inconnue  

---

## 🎯 Objectifs

### Objectif principal
Mettre en place un **système de reconnaissance faciale simple et fonctionnel**.

### Objectifs secondaires
- Détecter automatiquement les visages dans les images ou vidéos  
- Comparer les visages détectés avec ceux stockés dans la base de données  
- Afficher les informations associées à la personne reconnue  
- Gérer les cas où la personne n’est pas trouvée  

---

## ⚙️ Fonctionnalités

### Fonctionnalités principales
- Détection de visage (temps réel)  
- Reconnaissance faciale via encodage  
- Identification (personne connue / inconnue)  
- Affichage en direct avec annotations  

### Fonctionnalités secondaires
- Détection simultanée de plusieurs visages  
- Encadrement visuel des visages détectés  
- Affichage des résultats directement sur l’image  

---

## 🛠️ Technologies utilisées
- **Python**  
- **OpenCV (cv2)** – Détection de visage et traitement vidéo  
- **NumPy** – Calculs numériques  
- **face_recognition** *(ou MediaPipe en alternative)* – Encodage et comparaison des visages  

---

## 🧠 Architecture du système

### Entrée
- Flux vidéo webcam ou image  

### Traitement
1. Capture de l’image  
2. Détection des visages  
3. Extraction des caractéristiques faciales (encodage)  
4. Comparaison avec la base de données  

### Sortie
- Affichage des informations de la personne reconnue  
- Ou affichage : `"Personne introuvable"`  

---

## 🗂️ Structure de la base de données
Le système utilise une **base de données locale** :

\Images\
    -personne1.jpg
    -personne2.jpg
    .
    .
    .

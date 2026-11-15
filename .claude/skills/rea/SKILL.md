---
name: rea
description: Reserve Anything (REA) : trouve et prépare la réservation de n'importe quoi (hôtel, activité, restaurant, rendez-vous, billet, salle). Cherche les options, compare, puis prépare la réservation (lien, brouillon d'email, événement agenda) après validation. Ex : « rea hôtel à Lisbonne 12-15 déc », « réserve-moi un resto samedi ».
---

# REA : Reserve Anything

## 1. Cadrer (une seule question groupée si besoin)
Type (hébergement, activité, restaurant, RDV, autre), lieu, dates/heure, nombre de personnes, budget, contraintes. Si l'info est déjà donnée, ne pas la redemander.

## 2. Chercher
- Hébergement : `mcp__Booking_com__accommodations_search`
- Activités / attractions : `mcp__Booking_com__attractions_search`
- Questions sur un établissement : `mcp__Booking_com__answer_property_qa_by_ids_v2`
- Reste (restaurant, billets, etc.) : WebSearch
- Vérifier la disponibilité dans l'agenda : `mcp__Google_Calendar__list_events`

## 3. Comparer
Tableau de 3 à 5 options : prix total, note, localisation, annulation gratuite ou non, lien. Donner une recommandation claire.

## 4. Réserver (après choix explicite de l'utilisateur)
- Fournir le lien de réservation officiel : l'utilisateur finalise lui-même le paiement.
- Si réservation par email : `mcp__Gmail__create_draft` (brouillon uniquement, jamais d'envoi sans accord).
- Ajouter l'événement à l'agenda (`mcp__Google_Calendar__create_event`) une fois confirmé.

## Règles
- Ne jamais payer, envoyer un message ni créer d'événement sans validation explicite.
- Ne jamais dire qu'une réservation est faite si elle ne l'est pas : indiquer ce qui reste à faire.
- Annoncer clairement prix, conditions d'annulation et dates avant de valider.
- Réponses courtes, en français.

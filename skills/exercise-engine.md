# Exercise Engine

## When To Use
Use when the user asks about a specific exercise, wants exercise examples, or needs image-backed lookup from the local database.

## Database Detection
Check whether `exercise-db/exercises.json` exists before attempting structured lookup.

## Query Flow
Use the query script to filter by muscle or equipment, or fetch one exercise by id.

## Image Path Output
When a matching exercise contains an image path, return the local image path alongside the exercise name.

## Missing Database Fallback
If the database is unavailable, provide text-only exercise guidance and explain how to initialize the local exercise database.

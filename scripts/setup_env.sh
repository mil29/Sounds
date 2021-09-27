#!/bin/bash
touch .env
echo SECRET_KEY=${{ secrets.SECRET_KEY }} >> .env
echo AWS_ACCESS_KEY_ID=${{ secrets.AWS_ACCESS_KEY_ID }} >> .env
echo AWS_SECRET_ACCESS_KEY=${{ secrets.AWS_SECRET_ACCESS_KEY }} >> .env
echo EMAIL_HOST_PASSWORD=${{ secrets.EMAIL_HOST_PASSWORD }} >> .env
echo EMAIL_HOST_USER=${{ secrets.EMAIL_HOST_USER }} >> .env





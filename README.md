# Azure CMS Project

## Project Overview

This project demonstrates deploying a Flask-based Content Management System (CMS) on Microsoft Azure. The application allows users to create and view articles through a web interface.

## Azure Services Used

* Azure App Service (Hosting)
* Azure SQL Database (Article storage)
* Azure Blob Storage (Image storage)
* Microsoft Entra ID (Authentication)
* GitHub Actions (CI/CD deployment)

## Deployment Choice

I chose **Azure App Service instead of a Virtual Machine** because App Service simplifies deployment and management. It provides built-in support for Python web applications, automatic scaling, and easy integration with GitHub for continuous deployment. Using a VM would require manual configuration and server management, which is more complex.

## Database

The CMS stores articles in an Azure SQL Database.

Example query used:

SELECT * FROM articles;

## Application Features

* Create articles
* Store articles in SQL database
* Upload images to Blob Storage
* Authentication using Microsoft Entra ID
* Automatic deployment via GitHub Actions

## Live Application

https://cms-articles-2026-f2dwc4cng5fja5hq.centralus-01.azurewebsites.net

## Repository

https://github.com/Aadityamurti/-cms-azure-project-12

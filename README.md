**📊 Cloud Resume Challenge - Manoj**

Live Site: https://dlrl2fxutn5w1.cloudfront.net/

Created on: June 18, 2025

**Project Overview**

This project is my implementation of the Cloud Resume Challenge, designed to showcase my practical skills in Cloud, DevOps, and Serverless technologies.
The site is a static resume hosted on S3, secured via CloudFront, and includes a serverless visitor counter using Lambda, API Gateway, and DynamoDB.

**Architecture Diagram**

![Cloud resume drawio](https://github.com/user-attachments/assets/4794c35e-db3e-432e-9bb2-1767177d1a3f)

**Services Used**

* Amazon S3 (Static site hosting)
* Amazon CloudFront (CDN + HTTPS)
* AWS Lambda (Python visitor counter logic)
* Amazon DynamoDB (Visitor count data store)
* Amazon API Gateway (Trigger Lambda from browser)
* IAM (Roles and policies)

**Features**

* Fully serverless & free-tier eligible
* Auto-incrementing visitor counter
* S3-hosted resume served over HTTPS
* Public, portable, and scalable project

**How It Works**

* Static site is hosted in an S3 bucket
* CloudFront serves the site securely via HTTPS
* Visitor counter is implemented using JavaScript fetch()
* API Gateway triggers a Lambda function
* Lambda updates and returns count from DynamoDB
* JS updates the <span id="visitor-count"> on page

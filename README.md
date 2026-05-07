# ☁️ Cloud Fun Facts Generator

> A fully serverless, cloud-native web application that generates witty AI-powered cloud computing facts — built on AWS with Generative AI at its core.

[![AWS](https://img.shields.io/badge/Built%20on-AWS-FF9900?style=flat&logo=amazonaws&logoColor=white)](https://aws.amazon.com/)
[![Serverless](https://img.shields.io/badge/Architecture-Serverless-blueviolet?style=flat)](https://aws.amazon.com/serverless/)
[![Amazon Bedrock](https://img.shields.io/badge/AI-Amazon%20Bedrock-green?style=flat)](https://aws.amazon.com/bedrock/)
[![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)]()

---

## 📌 Overview

The Cloud Fun Facts Generator lets users instantly generate AI-crafted, witty cloud computing facts through a clean, responsive frontend hosted on AWS Amplify.

**How it works — one click, five services:**

1. The user clicks **Generate Fun Fact** on the frontend
2. The frontend sends a request to **Amazon API Gateway** (HTTP API)
3. API Gateway triggers an **AWS Lambda** function
4. Lambda fetches a cloud fact from **Amazon DynamoDB**
5. **Amazon Bedrock** (Nova Lite model) rewrites it into a witty AI response
6. The generated fact is returned and displayed on screen

---

## 🏗️ Architecture Diagram

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/259e5cb9-ae8c-42ff-939e-3aca7579550a" />

## 🌐 Final Result
This is what your project will look like once built:

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/0152a39c-cbe5-47bb-a4ee-1042d13df6d0" />

---

## 🎥 Demo

[▶️ Watch Demo Video](ADD_VIDEO_LINK_HERE)

---

## 🛠️ AWS Services Used

| Service | Role in the Project |
|---|---|
| **AWS Lambda** | Serverless backend — processes requests and orchestrates responses |
| **Amazon API Gateway** | Exposes a RESTful HTTP API endpoint for the frontend |
| **Amazon DynamoDB** | Stores a library of cloud computing facts |
| **Amazon Bedrock** | Generates witty, AI-powered rewordings using the Nova Lite model |
| **AWS Amplify** | Hosts and deploys the frontend application |
| **AWS IAM** | Manages permissions and access control across services |

---

## ✨ Features

- ⚡ Fully serverless — no servers to manage, scales automatically
- 🤖 Generative AI integration via Amazon Bedrock (Nova Lite)
- 🗄️ DynamoDB-backed fact storage with Lambda retrieval
- 🌐 HTTP API Gateway simple cheaper than REST API
- 🖥️ Responsive frontend hosted on AWS Amplify
- 🔒 Secure IAM permission model across all services
- 💸 Designed to stay within AWS Free Tier limits

---

## ⚙️ Setup & Deployment

### Deployment Steps

#### 1. Create the DynamoDB Table
- Table name: `CloudFacts`
- Partition key: `factId` (String)
- Populate the table with cloud computing fact records
<img width="800" height="400" alt="img10" src="https://github.com/user-attachments/assets/d3bcd4fc-81a8-4e0e-8643-3524141e8fd0" />

<img width="800" height="400" alt="img11" src="https://github.com/user-attachments/assets/c7678caa-2871-44a5-9246-171b26bae68c" />

#### 2. Create the Lambda Function
- Runtime: **Python 3.x**
- Attach an IAM role with permissions for DynamoDB and Bedrock
- Deploy the function from `lambda/lambda_function.py`
  
<img width="800" height="400" alt="img1" src="https://github.com/user-attachments/assets/03ba197f-528f-4339-ae30-5176128888c9" />

<img width="800" height="400" alt="Screenshot 2026-05-06 103811" src="https://github.com/user-attachments/assets/69f9f5ae-d2fe-4c42-b155-93da47e9dba2" />

<img width="800" height="400" alt="Screenshot 2026-05-06 104325" src="https://github.com/user-attachments/assets/b662418e-872b-41e7-965b-73d3133e40b9" />

#### 3. Set Up API Gateway (HTTP API)
- Create a new **HTTP API**
- Add a `GET /funfact` route
- Integrate the route with the Lambda function
- Enable **CORS** for the Amplify frontend origin
<img width="800" height="400" alt="img7" src="https://github.com/user-attachments/assets/01cb3dfe-9d9f-491d-a30e-32b53d9ad6df" />

<img width="800" height="200" alt="img8" src="https://github.com/user-attachments/assets/ca9ecef5-27af-46a7-ab1f-123791d97125" />

<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/c6bc2e83-61fb-4475-a88d-c8b9661eafec" />

#### 4. Configure Amazon Bedrock
- Enable model access in the AWS Console by submiting onetime usecase and provide IAM permissions
- Select and enable the **Amazon Nova Lite** model
- Update the Lambda function with the correct model ID and inference parameters
  
<img width="800" height="400" alt="Screenshot 2026-05-06 104212" src="https://github.com/user-attachments/assets/dd9fb0b0-2d60-4961-9ec4-206be67c1a93" />

#### 5. Deploy the Frontend via AWS Amplify
- Upload `frontend/index.html` to a new Amplify app
- Update the API endpoint URL in the frontend code
- Trigger a deployment and verify the live URL
<img width="800" height="400" alt="img13" src="https://github.com/user-attachments/assets/0efb1f19-5a04-450c-b1a3-08d90477d733" />

---

## 📁 Project Structure

```
CloudFunFactGenerator/
│
├── lambda/
│   └── lambda_function.py       # Core backend logic
│
├── frontend/
│   └── index.html               # Frontend UI
│
├── architecture/
│   └── architecture-diagram.png # Architecture diagram
│
└── README.md
```

---

## 🚧 Challenges & How They Were Solved

| Challenge | Resolution |
|---|---|
| CORS errors between Amplify and API Gateway | Configured CORS headers correctly on the HTTP API |
| IAM permission issues for DynamoDB and Bedrock | Scoped IAM role with least-privilege policies |
| Bedrock model deprecation mid-project | Migrated from legacy model to **Amazon Nova Lite** |
| API Gateway route not resolving | Debugged route configuration and redeployed the stage |
| Bedrock inference compatibility errors | Updated invocation payload to match Nova Lite's expected format |
| Frontend deployment failures on Amplify | Resolved by correcting build settings and re-uploading the app |

---

## 📚 Key Learnings

- Designing and wiring together a multi-service serverless architecture on AWS
- Integrating Generative AI into a real application using Amazon Bedrock
- Working with HTTP APIs in API Gateway and managing CORS in serverless deployments
- Writing Lambda functions that interface with both DynamoDB and Bedrock
- Structuring IAM roles and policies for least-privilege access
- Diagnosing and resolving real-world cloud deployment issues end-to-end

---

## 🚀 Future Improvements

- [ ] Add user authentication with **Amazon Cognito**
- [ ] Automate infrastructure provisioning with **Terraform**
- [ ] Set up a **CI/CD pipeline** using GitHub Actions
- [ ] Add multiple AI-generated fact categories (e.g., DevOps, Security, Networking)
- [ ] Store and display a history of previously generated facts
- [ ] Build an analytics dashboard using CloudWatch metrics
- [ ] Improve the frontend UI/UX with a modern component library

---

## 💰 Cost Considerations

This project was designed to stay within **AWS Free Tier** limits wherever possible:

| Service | Cost Profile |
|---|---|
| AWS Lambda | Free Tier eligible (1M requests/month free) |
| Amazon API Gateway | Low-cost HTTP API pricing |
| Amazon DynamoDB | Free Tier eligible (25 GB storage free) |
| AWS Amplify | Free Tier eligible for hosting |
| Amazon Bedrock | Pay-per-use inference — minimal cost for testing |

---
# 🧹 Cleanup Steps

To avoid AWS charges, delete the following resources after testing:

- AWS Amplify App
- API Gateway HTTP API (`FunfactsAPI`)
- Lambda Function (`CloudFunFacts`)
- DynamoDB Table (`CloudFacts`)
- CloudWatch Log Groups (`/aws/lambda/CloudFunFacts`)
- Optional: IAM roles created for the project

> Note: Amazon Bedrock is usage-based, so avoid unnecessary model invocations.


## 👩‍💻 Author

**Deepigha Japamony**

---


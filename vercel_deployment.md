# 🚀 Step-by-Step Vercel Deployment Guide

Follow these steps to deploy your Heart Disease Prediction frontend to Vercel.

### 1. Log in to Vercel
Go to [vercel.com](https://vercel.com/) and log in with your **GitHub account**.

### 2. Add New Project
1. On your Vercel Dashboard, click the **"Add New..."** button and select **"Project"**.
2. You will see a list of your GitHub repositories. Find and click **"Import"** next to `heart-disease-logistic`.

### 3. Configure Project (CRITICAL)
This is the most important step to make sure Vercel finds your website:
1. **Project Name**: You can leave this as `heart-disease-logistic`.
2. **Framework Preset**: Select **"Other"** (since it's a simple HTML/JS project).
3. **Root Directory**: 
   - Click **"Edit"**.
   - Select the **`frontend`** folder.
   - Click **"Continue"**.
4. **Build and Output Settings**: You don't need to change anything here.

### 4. Deploy
Click the **"Deploy"** button. Vercel will build your project in about 30-60 seconds.

### 5. Your Application is Live!
Once finished, you will see a preview of your site and a button that says **"Continue to Dashboard"**. Your live URL will look something like:
`https://heart-disease-logistic.vercel.app`

---

### ✅ Verification Checklist
- [ ] Open your new Vercel link.
- [ ] Enter sample data in the form.
- [ ] Click "Analyze Health Status".
- [ ] Ensure it displays the prediction (this confirms it's talking to your Render backend).

**Congratulations! Your project is fully deployed.**

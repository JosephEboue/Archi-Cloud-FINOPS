# Lab 11: Implementing Azure Monitor and Alerts
Azure Monitor helps you maximize the availability and performance of your applications and services by collecting, analyzing, and acting on telemetry data. In this lab, you will configure Azure Monitor to collect metrics and logs, create alerts based on metrics, visualize the data using Azure dashboards, and configure Action Groups for notification purposes.

#### Prerequisites
- An active Azure Subscription.
- Basic knowledge of Azure services and monitoring tools.
- Access to the Azure Portal.
## Step 1 : Set up Azure Monitor to Collect Metrics and Logs 
- Log in to the Azure Portal:
- Navigate to Azure Monitor:
- Enable Diagnostic Settings:
![Diagnostic setting](dignostic-setting.png)
![log analytics](log-analytics.png)

## Step 2 : Create alerts based on resource metrics
- Go to Azure Monitor Alerts
- Define the Alert Rule
![Alert Rule](alert-rule.png)
- Create the Alert
![Create Alert Rule](log-alert-rule.png)
![Alert Rule Reult](dashboard.png)

## Step 3 : Visualize Data Using Azure Dashboards
- Create a New Dashboard
![Create Dashboard](create-dash.png)
- Add Metrics and Logs
![Add tiles](add-metrics.png)
- Customize the Dashboard
![Dashboard](dashboard0.png)
- Share the Dashboard
![Share Dashboard](share-dash.png)

## Step 4 : Implement Action Groups for alert notifications
- Create an Action Group
![Action group](action-group.png)
- Configure the Action Group
- Test the Action Group through email
![Test Action group](test.png)

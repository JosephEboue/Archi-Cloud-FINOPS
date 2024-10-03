# Lab 12: Using Azure Resource Manager (ARM) Templates
Azure Resource Manager (ARM) templates allow for declarative management of resources in Azure.

## Step 1 : Create the ARM Template
    An ARM template is a JSON file that defines the resources you want to deploy. Below is a sample structure of an ARM template for a multi-tier application with a web server and database:
- Create the ARM Template
    This template creates a basic virtual machine and an Azure SQL database server. You can add other resources such as networking and storage as needed.
- Save the Template
    Save this file as azuredeploy.json in your working directory.

## Step 2 : Parameterize the Template for Reusability
- Add Parameters : 
    In the parameters section of the ARM template, define parameters for values such as VM names, sizes, admin credentials, and more. This allows you to reuse the template for different environments
- Modify Resource Definitions
    Use these parameters in the resource definitions to make the template adaptable
    Example:
    ```bash
    "name": "[parameters('vmName')]",
    "location": "[resourceGroup().location]"
    ```
## Step 3 : Deploy Resources Using the Template via Azure CLI
- Deploy the Template
```bash
az login
az deployment group create --resource-group <ResourceGroupName> --template-file azuredeploy.json --parameters @azuredeploy.parameters.json
az deployment group create --resource-group <ResourceGroupName> --template-file azuredeploy.json --parameters vmName="myVM" adminUsername="adminUser" adminPassword="P@ssword123!"
```

## Step 4 : Validate and troubleshoot deployment issues.
- Check Deployment Status
```bash
    az deployment group show --resource-group <ResourceGroupName>
```
- Check for Errors
    If the deployment fails, you can review detailed error messages in the CLI or Azure Portal. Errors could be due to incorrect parameters, missing dependencies, or Azure service limitations.
- Troubleshoot Common Issues
```bash
    az upgrade
```
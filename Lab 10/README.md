# Lab 10: Configuring Azure Backup and Recovery Services
## Step 1 : Create a Recovery Services Vault
After logging in, Search for Recovery Services Vault and create a new vault
![vault](vault.png)

## Step 2 : Configure Backup for VMs
![VM backup](myVm-backup.png)

## Step 3 : Configure Backup for Azure Files
The following shows how i can configure backup for individual file shares from the respective file share blade:
![Backup Azure Files](file-sto.png)
![Backup Azure Files](file-share-backup.png)
![Backup Azure Files](file-share-backup-policy.png)

## Step 3 : Perform Backup and Restore Operations
To run an on-demamd backup, follow these steps:
Open the file share’s Overview blade for which you want to take an on-demand backup.
Under the Operation section, select Backup.
The context blade appears on the right that lists Vault Essentials. Select Backup Now to take an on-demand backup.
![Backup Azure Files](backup-now.png)


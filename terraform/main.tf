data "azurerm_resource_group" "asg" {
  name = var.asg
}

resource "azurerm_storage_account" "swisspine_storage_account" {
  name                     = "swisspinestorageaccount"
  resource_group_name      = data.azurerm_resource_group.asg.name
  location                 = data.azurerm_resource_group.asg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "swisspine_blob_storage" {
  name                  = "swisspineblobstorage"
  storage_account_name  = azurerm_storage_account.swisspine_storage_account.name
  container_access_type = "private"
}
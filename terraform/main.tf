data "azurerm_resource_group" "asg" {
  name = var.asg
}

resource "azurerm_storage_account" "swisspine_storage" {
  name                     = "swisspine_storage"
  resource_group_name      = data.azurerm_resource_group.asg.name
  location                 = data.azurerm_resource_group.asg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
variable "location" {
  default = "westeurope"
}

variable "resource_group_name" {
  default = "rg-CP2alex"
}

variable "acr_name" {
  default = "acrCP2alex"
}

variable "aks_name" {
  type        = string
  description = "Alejandro Ortiz AKS"
  default     = "aks-alex-cp2"
}

variable "aks_node_count" {
  type    = number
  default = 1
}

variable "aks_vm_size" {
  type    = string
  default = "Standard_B2s"
}

variable "aks_dns_prefix" {
  type    = string
  default = "aks-alex-cp2"
}

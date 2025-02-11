# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['network private-dns'] = """
type: group
short-summary: Manage Private DNS domains in Azure.
"""

helps['network private-dns link'] = """
type: group
short-summary: Manage Private DNS links.
"""

helps['network private-dns link vnet'] = """
type: group
short-summary: Manage virtual network links to the specified Private DNS zone.
"""

helps['network private-dns link vnet create'] = """
type: command
short-summary: Create a virtual network link to the specified Private DNS zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the virtual network link.
examples:
  - name: Create a virtual network link to the specified Private DNS zone.
    text: |
        az network private-dns link vnet create -g MyResourceGroup -n MyLinkName -z www.mysite.com \\
            -v MyVirtualNetworkId -e False
"""

helps['network private-dns link vnet delete'] = """
type: command
short-summary: Delete a virtual network link to the specified Private DNS zone.
long-summary: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone.
examples:
  - name: Delete a virtual network link to the specified Private DNS zone.
    text: >
        az network private-dns link vnet delete -g MyResourceGroup -z www.mysite.com -n MyLinkName
"""

helps['network private-dns link vnet list'] = """
type: command
short-summary: List the virtual network links to the specified Private DNS zone.
examples:
  - name: List virtual network links to the specified Private DNS zone in a resource group.
    text: >
        az network private-dns link vnet list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns link vnet show'] = """
type: command
short-summary: Get a virtual network link to the specified Private DNS zone.
examples:
  - name: Get a virtual network link to the specified Private DNS zone..
    text: >
        az network private-dns link vnet show -g MyResourceGroup -n MyLinkName -z www.mysite.com
"""

helps['network private-dns link vnet update'] = """
type: command
short-summary: Update a virtual network link's properties. Does not modify virtual network within the link.
parameters:
  - name: --tags
    short-summary: Resource tags for the virtual network link.
  - name: --if-match
    short-summary: The ETag of the virtual network link to the Private DNS zone.
    long-summary: Omit this value to always overwrite the current virtual network link.
                  Specify the last-seen ETag value to prevent accidentally overwritting any concurrent changes.
examples:
  - name: Update a virtual network link properties to enable registration.
    text: >
        az network private-dns link vnet update -g MyResourceGroup -n MyLinkName -z www.mysite.com -e True
"""

helps['network private-dns link vnet wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the virtual network link to the specified Private DNS zone is met.
examples:
  - name: Pause executing next line of CLI script until the virtual network link to the specified Private DNS zone is successfully provisioned.
    text: az network private-dns link vnet wait -g MyResourceGroup -n MyLinkName -z www.mysite.com --created
"""

helps['network private-dns record-set'] = """
type: group
short-summary: Manage Private DNS records and record sets.
"""

helps['network private-dns record-set a'] = """
type: group
short-summary: Manage Private DNS A records.
"""

helps['network private-dns record-set a add-record'] = """
type: command
short-summary: Add an A record.
examples:
  - name: Add an A record.
    text: |
        az network private-dns record-set a add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network private-dns record-set a create'] = """
type: command
short-summary: Create an empty A record set.
examples:
  - name: Create an empty A record set.
    text: az network private-dns record-set a create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set a delete'] = """
type: command
short-summary: Delete an A record set and all associated records.
examples:
  - name: Delete an A record set and all associated records.
    text: az network private-dns record-set a delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set a list'] = """
type: command
short-summary: List all A record sets in a zone.
examples:
  - name: List all A record sets in a zone.
    text: az network private-dns record-set a list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set a remove-record'] = """
type: command
short-summary: Remove an A record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an A record from its record set.
    text: |
        az network private-dns record-set a remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv4Address
"""

helps['network private-dns record-set a show'] = """
type: command
short-summary: Get the details of an A record set.
examples:
  - name: Get the details of an A record set.
    text: az network private-dns record-set a show -g MyResourceGroup -n MyRecordSet -z www.mysite.com
"""

helps['network private-dns record-set a update'] = """
type: command
short-summary: Update an A record set.
examples:
  - name: Update an A record set.
    text: |
        az network private-dns record-set a update -g MyResourceGroup -n MyRecordSet \\
            -z www.mysite.com --metadata owner=WebTeam
  - name: Update an A record set. (autogenerated)
    text: az network private-dns record-set a update --name MyRecordSet --resource-group MyResourceGroup --set useRemoteGateways=true --zone-name www.mysite.com
    crafted: true
"""

helps['network private-dns record-set aaaa'] = """
type: group
short-summary: Manage Private DNS AAAA records.
"""

helps['network private-dns record-set aaaa add-record'] = """
type: command
short-summary: Add an AAAA record.
examples:
  - name: Add an AAAA record.
    text: |
        az network private-dns record-set aaaa add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network private-dns record-set aaaa create'] = """
type: command
short-summary: Create an empty AAAA record set.
examples:
  - name: Create an empty AAAA record set.
    text: az network private-dns record-set aaaa create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa delete'] = """
type: command
short-summary: Delete an AAAA record set and all associated records.
examples:
  - name: Delete an AAAA record set and all associated records.
    text: az network private-dns record-set aaaa delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa list'] = """
type: command
short-summary: List all AAAA record sets in a zone.
examples:
  - name: List all AAAA record sets in a zone.
    text: az network private-dns record-set aaaa list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set aaaa remove-record'] = """
type: command
short-summary: Remove AAAA record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an AAAA record from its record set.
    text: |
        az network private-dns record-set aaaa remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -a MyIpv6Address
"""

helps['network private-dns record-set aaaa show'] = """
type: command
short-summary: Get the details of an AAAA record set.
examples:
  - name: Get the details of an AAAA record set.
    text: az network private-dns record-set aaaa show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set aaaa update'] = """
type: command
short-summary: Update an AAAA record set.
examples:
  - name: Update an AAAA record set.
    text: |
        az network private-dns record-set aaaa update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set cname'] = """
type: group
short-summary: Manage Private DNS CNAME records.
"""

helps['network private-dns record-set cname create'] = """
type: command
short-summary: Create an empty CNAME record set.
examples:
  - name: Create an empty CNAME record set.
    text: az network private-dns record-set cname create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname delete'] = """
type: command
short-summary: Delete a CNAME record set and its associated record.
examples:
  - name: Delete a CNAME record set and its associated record.
    text: az network private-dns record-set cname delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname list'] = """
type: command
short-summary: List the CNAME record set in a zone.
examples:
  - name: List the CNAME record set in a zone.
    text: az network private-dns record-set cname list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set cname remove-record'] = """
type: command
short-summary: Remove a CNAME record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a CNAME record from its record set.
    text: |
        az network private-dns record-set cname remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network private-dns record-set cname set-record'] = """
type: command
short-summary: Set the value of a CNAME record.
examples:
  - name: Set the value of a CNAME record.
    text: |
        az network private-dns record-set cname set-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -c www.contoso.com
"""

helps['network private-dns record-set cname show'] = """
type: command
short-summary: Get the details of a CNAME record set.
examples:
  - name: Get the details of a CNAME record set.
    text: az network private-dns record-set cname show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set cname update'] = """
type: command
short-summary: Update a CNAME record set.
examples:
  - name: Update a CNAME record set.
    text: |
        az network private-dns record-set cname update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set list'] = """
type: command
short-summary: List all record sets within a Private DNS zone.
examples:
  - name: List all "@" record sets within this zone.
    text: |
        az network private-dns record-set list -g MyResourceGroup -z www.mysite.com \\
            --query "[?name=='@']"
"""

helps['network private-dns record-set mx'] = """
type: group
short-summary: Manage Private DNS MX records.
"""

helps['network private-dns record-set mx add-record'] = """
type: command
short-summary: Add an MX record.
examples:
  - name: Add an MX record.
    text: |
        az network private-dns record-set mx add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network private-dns record-set mx create'] = """
type: command
short-summary: Create an empty MX record set.
examples:
  - name: Create an empty MX record set.
    text: az network private-dns record-set mx create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx delete'] = """
type: command
short-summary: Delete an MX record set and all associated records.
examples:
  - name: Delete an MX record set and all associated records.
    text: az network private-dns record-set mx delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx list'] = """
type: command
short-summary: List all MX record sets in a zone.
examples:
  - name: List all MX record sets in a zone.
    text: az network private-dns record-set mx list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set mx remove-record'] = """
type: command
short-summary: Remove an MX record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an MX record from its record set.
    text: |
        az network private-dns record-set mx remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -e mail.mysite.com -p 10
"""

helps['network private-dns record-set mx show'] = """
type: command
short-summary: Get the details of an MX record set.
examples:
  - name: Get the details of an MX record set.
    text: az network private-dns record-set mx show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set mx update'] = """
type: command
short-summary: Update an MX record set.
examples:
  - name: Update an MX record set.
    text: |
        az network private-dns record-set mx update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set ptr'] = """
type: group
short-summary: Manage Private DNS PTR records.
"""

helps['network private-dns record-set ptr add-record'] = """
type: command
short-summary: Add a PTR record.
examples:
  - name: Add a PTR record.
    text: |
        az network private-dns record-set ptr add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network private-dns record-set ptr create'] = """
type: command
short-summary: Create an empty PTR record set.
examples:
  - name: Create an empty PTR record set.
    text: az network private-dns record-set ptr create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr delete'] = """
type: command
short-summary: Delete a PTR record set and all associated records.
examples:
  - name: Delete a PTR record set and all associated records.
    text: az network private-dns record-set ptr delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr list'] = """
type: command
short-summary: List all PTR record sets in a zone.
examples:
  - name: List all PTR record sets in a zone.
    text: az network private-dns record-set ptr list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set ptr remove-record'] = """
type: command
short-summary: Remove a PTR record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a PTR record from its record set.
    text: |
        az network private-dns record-set ptr remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -d another.site.com
"""

helps['network private-dns record-set ptr show'] = """
type: command
short-summary: Get the details of a PTR record set.
examples:
  - name: Get the details of a PTR record set.
    text: az network private-dns record-set ptr show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set ptr update'] = """
type: command
short-summary: Update a PTR record set.
examples:
  - name: Update a PTR record set.
    text: |
        az network private-dns record-set ptr update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set soa'] = """
type: group
short-summary: Manage Private DNS SOA record.
"""

helps['network private-dns record-set soa show'] = """
type: command
short-summary: Get the details of an SOA record.
examples:
  - name: Get the details of an SOA record.
    text: az network private-dns record-set soa show -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set soa update'] = """
type: command
short-summary: Update properties of an SOA record.
examples:
  - name: Update properties of an SOA record.
    text: |
        az network private-dns record-set soa update -g MyResourceGroup -z www.mysite.com \\
            -e myhostmaster.mysite.com
"""

helps['network private-dns record-set srv'] = """
type: group
short-summary: Manage Private DNS SRV records.
"""

helps['network private-dns record-set srv add-record'] = """
type: command
short-summary: Add an SRV record.
examples:
  - name: Add an SRV record.
    text: |
        az network private-dns record-set srv add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network private-dns record-set srv create'] = """
type: command
short-summary: Create an empty SRV record set.
examples:
  - name: Create an empty SRV record set.
    text: |
        az network private-dns record-set srv create -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet
"""

helps['network private-dns record-set srv delete'] = """
type: command
short-summary: Delete an SRV record set and all associated records.
examples:
  - name: Delete an SRV record set and all associated records.
    text: az network private-dns record-set srv delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set srv list'] = """
type: command
short-summary: List all SRV record sets in a zone.
examples:
  - name: List all SRV record sets in a zone.
    text: az network private-dns record-set srv list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set srv remove-record'] = """
type: command
short-summary: Remove an SRV record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove an SRV record from its record set.
    text: |
        az network private-dns record-set srv remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -t webserver.mysite.com -r 8081 -p 10 -w 10
"""

helps['network private-dns record-set srv show'] = """
type: command
short-summary: Get the details of an SRV record set.
examples:
  - name: Get the details of an SRV record set.
    text: az network private-dns record-set srv show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set srv update'] = """
type: command
short-summary: Update an SRV record set.
examples:
  - name: Update an SRV record set.
    text: |
        az network private-dns record-set srv update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns record-set txt'] = """
type: group
short-summary: Manage Private DNS TXT records.
"""

helps['network private-dns record-set txt add-record'] = """
type: command
short-summary: Add a TXT record.
examples:
  - name: Add a TXT record.
    text: |
        az network private-dns record-set txt add-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network private-dns record-set txt create'] = """
type: command
short-summary: Create an empty TXT record set.
examples:
  - name: Create an empty TXT record set.
    text: az network private-dns record-set txt create -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt delete'] = """
type: command
short-summary: Delete a TXT record set and all associated records.
examples:
  - name: Delete a TXT record set and all associated records.
    text: az network private-dns record-set txt delete -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt list'] = """
type: command
short-summary: List all TXT record sets in a zone.
examples:
  - name: List all TXT record sets in a zone.
    text: az network private-dns record-set txt list -g MyResourceGroup -z www.mysite.com
"""

helps['network private-dns record-set txt remove-record'] = """
type: command
short-summary: Remove a TXT record from its record set.
long-summary: >
    By default, if the last record in a set is removed, the record set is deleted.
    To retain the empty record set, include --keep-empty-record-set.
examples:
  - name: Remove a TXT record from its record set.
    text: |
        az network private-dns record-set txt remove-record -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet -v Owner=WebTeam
"""

helps['network private-dns record-set txt show'] = """
type: command
short-summary: Get the details of a TXT record set.
examples:
  - name: Get the details of a TXT record set.
    text: az network private-dns record-set txt show -g MyResourceGroup -z www.mysite.com -n MyRecordSet
"""

helps['network private-dns record-set txt update'] = """
type: command
short-summary: Update a TXT record set.
examples:
  - name: Update a TXT record set.
    text: |
        az network private-dns record-set txt update -g MyResourceGroup -z www.mysite.com \\
            -n MyRecordSet --metadata owner=WebTeam
"""

helps['network private-dns zone'] = """
type: group
short-summary: Manage Private DNS zones.
"""

helps['network private-dns zone create'] = """
type: command
short-summary: Create a Private DNS zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the Private DNS zone.
examples:
  - name: Create a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone create -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone delete'] = """
type: command
short-summary: Delete a Private DNS zone.
long-summary: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed.
examples:
  - name: Delete a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone delete -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone list'] = """
type: command
short-summary: List Private DNS zones.
examples:
  - name: List Private DNS zones in a resource group.
    text: >
        az network private-dns zone list -g MyResourceGroup
"""

helps['network private-dns zone show'] = """
type: command
short-summary: Get a Private DNS zone.
examples:
  - name: Get a Private DNS zone using a fully qualified domain name.
    text: >
        az network private-dns zone show -g MyResourceGroup -n www.mysite.com
"""

helps['network private-dns zone update'] = """
type: command
short-summary: Update a Private DNS zone's properties. Does not modify Private DNS records or virtual network links within the zone.
parameters:
  - name: --tags
    short-summary: Resource tags for the Private DNS zone.
examples:
  - name: Update a Private DNS zone properties to change the user-defined value of a previously set tag.
    text: >
        az network private-dns zone update -g MyResourceGroup -n www.mysite.com --tags CostCenter=Marketing
"""

helps['network private-dns zone wait'] = """
type: command
short-summary: Place the CLI in a waiting state until a condition of the Private DNS zone is met.
examples:
  - name: Pause executing next line of CLI script until the Private DNS zone is successfully provisioned.
    text: az network private-dns zone wait -g MyResourceGroup -n www.mysite.com --created
"""

# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long, too-many-lines

from knack.help_files import helps


helps['ams'] = """
    type: group
    short-summary: Manage Azure Media Services resources.
"""

helps['ams account'] = """
    type: group
    short-summary: Manage Azure Media Services accounts.
"""

helps['ams account create'] = """
    type: command
    short-summary: Create an Azure Media Services account.
"""

helps['ams account update'] = """
    type: command
    short-summary: Update the details of an Azure Media Services account.
"""

helps['ams account list'] = """
    type: command
    short-summary: List Azure Media Services accounts for the entire subscription.
"""

helps['ams account show'] = """
    type: command
    short-summary: Show the details of an Azure Media Services account.
"""

helps['ams account delete'] = """
    type: command
    short-summary: Delete an Azure Media Services account.
"""

helps['ams account check-name'] = """
    type: command
    short-summary: Checks whether the Media Service resource name is available.
"""

helps['ams account storage'] = """
    type: group
    short-summary: Manage storage for an Azure Media Services account.
"""

helps['ams account storage add'] = """
    type: command
    short-summary: Attach a secondary storage to an Azure Media Services account.
"""

helps['ams account storage remove'] = """
    type: command
    short-summary: Detach a secondary storage from an Azure Media Services account.
"""

helps['ams account sp'] = """
    type: group
    short-summary: Manage service principal and role based access for an Azure Media Services account.
"""

helps['ams account sp create'] = """
    type: command
    short-summary: Create a service principal and configure its access to an Azure Media Services account.
    long-summary: Service principal propagation throughout Azure Active Directory may take some extra seconds to complete.
    examples:
        - name: Create a service principal with password and configure its access to an Azure Media Services account. Output will be in xml format.
          text: >
            az ams account sp create -a myAmsAccount -g myRG -n mySpName --password mySecret --role Owner --xml
    """

helps['ams account sp reset-credentials'] = """
    type: command
    short-summary: Generate a new client secret for a service principal configured for an Azure Media Services account.
"""

helps['ams account storage sync-storage-keys'] = """
    type: command
    short-summary: Synchronize storage account keys for a storage account associated with an Azure Media Services account.
"""

helps['ams transform'] = """
    type: group
    short-summary: Manage transforms for an Azure Media Services account.
"""

helps['ams transform list'] = """
    type: command
    short-summary: List all the transforms of an Azure Media Services account.
"""

helps['ams transform show'] = """
    type: command
    short-summary: Show the details of a transform.
"""

helps['ams transform create'] = """
    type: command
    short-summary: Create a transform.
    examples:
        - name: Create a transform with AdaptiveStreaming built-in preset and High relative priority.
          text: >
            az ams transform create -a myAmsAccount -n transformName -g myResourceGroup --preset AdaptiveStreaming --relative-priority High
        - name: Create a transform with a custom Standard Encoder preset from a JSON file and Low relative priority.
          text: >
            az ams transform create -a myAmsAccount -n transformName -g myResourceGroup --preset \"C:\\MyPresets\\CustomPreset.json\" --relative-priority Low
    """

helps['ams transform delete'] = """
    type: command
    short-summary: Delete a transform.
"""

helps['ams transform update'] = """
    type: command
    short-summary: Update the details of a transform.
    examples:
        - name: Update the first transform output of a transform by setting its relative priority to High.
          text: >
            az ams transform update -a myAmsAccount -n transformName -g myResourceGroup --set outputs[0].relativePriority=High
    """

helps['ams transform output'] = """
    type: group
    short-summary: Manage transform outputs for an Azure Media Services account.
"""

helps['ams transform output add'] = """
    type: command
    short-summary: Add an output to an existing transform.
    examples:
        - name: Add an output with a custom Standard Encoder preset from a JSON file.
          text: >
            az ams transform output add -a myAmsAccount -n transformName -g myResourceGroup --preset \"C:\\MyPresets\\CustomPreset.json\"
        - name: Add an output with a VideoAnalyzer preset with es-ES as audio language and only with audio insights.
          text: >
            az ams transform output add -a myAmsAccount -n transformName -g myResourceGroup --preset VideoAnalyzer --audio-language es-ES --insights-to-extract AudioInsightsOnly
    """

helps['ams transform output remove'] = """
    type: command
    short-summary: Remove an output from an existing transform.
    examples:
        - name: Remove the output element at the index specified with --output-index argument.
          text: >
            az ams transform output remove -a myAmsAccount -n transformName -g myResourceGroup --output-index 1
"""

helps['ams asset'] = """
    type: group
    short-summary: Manage assets for an Azure Media Services account.
"""

helps['ams asset-filter'] = """
    type: group
    short-summary: Manage asset filters for an Azure Media Services account.
"""

helps['ams account-filter'] = """
    type: group
    short-summary: Manage account filters for an Azure Media Services account.
"""

helps['ams asset show'] = """
    type: command
    short-summary: Show the details of an asset.
"""

helps['ams asset list'] = """
    type: command
    short-summary: List all the assets of an Azure Media Services account.
    examples:
        - name: List all the assets whose names start with the string 'Something'.
          text: >
            az ams asset list -a amsAccount -g resourceGroup --query [?starts_with(name,'Something')]
"""

helps['ams asset list-streaming-locators'] = """
    type: command
    short-summary: List streaming locators which are associated with this asset.
"""

helps['ams asset create'] = """
    type: command
    short-summary: Create an asset.
"""

helps['ams asset update'] = """
    type: command
    short-summary: Update the details of an asset.
"""

helps['ams asset delete'] = """
    type: command
    short-summary: Delete an asset.
"""

helps['ams asset get-sas-urls'] = """
    type: command
    short-summary: Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.
"""

helps['ams asset get-encryption-key'] = """
    type: command
    short-summary: Get the asset storage encryption keys used to decrypt content created by version 2 of the Media Services API.
"""

helps['ams asset-filter create'] = """
    type: command
    short-summary: Create an asset filter.
    examples:
        - name: Create an asset filter with filter track selections.
          text: >
            az ams asset-filter create -a amsAccount -g resourceGroup -n filterName --force-end-timestamp=False --end-timestamp 200000 --start-timestamp 100000 --live-backoff-duration 60 --presentation-window-duration 600000 --timescale 1000 --first-quality 720 --asset-name assetName --tracks @C:\\tracks.json
"""

helps['ams asset-filter update'] = """
    type: command
    short-summary: Update the details of an asset filter.
"""

helps['ams asset-filter delete'] = """
    type: command
    short-summary: Delete an asset filter.
"""

helps['ams asset-filter list'] = """
    type: command
    short-summary: List all the asset filters of an Azure Media Services account.
"""

helps['ams asset-filter show'] = """
    type: command
    short-summary: Show the details of an asset filter.
"""

helps['ams content-key-policy'] = """
    type: group
    short-summary: Manage content key policies for an Azure Media Services account.
"""

helps['ams content-key-policy create'] = """
    type: command
    short-summary: Create a new content key policy.
"""

helps['ams content-key-policy show'] = """
    type: command
    short-summary: Show an existing content key policy.
"""

helps['ams content-key-policy delete'] = """
    type: command
    short-summary: Delete a content key policy.
"""

helps['ams content-key-policy update'] = """
    type: command
    short-summary: Update an existing content key policy.
    examples:
        - name: Update an existing content-key-policy, set a new description and edit its first option setting a new issuer and audience.
          text: >
            az ams content-key-policy update -n contentKeyPolicyName -a amsAccount --description newDescription --set options[0].restriction.issuer=newIssuer --set options[0].restriction.audience=newAudience
"""

helps['ams content-key-policy list'] = """
    type: command
    short-summary: List all the content key policies within an Azure Media Services account.
"""

helps['ams content-key-policy option'] = """
    type: group
    short-summary: Manage options for an existing content key policy.
"""

helps['ams content-key-policy option add'] = """
    type: command
    short-summary: Add a new option to an existing content key policy.
"""

helps['ams content-key-policy option remove'] = """
    type: command
    short-summary: Remove an option from an existing content key policy.
"""

helps['ams content-key-policy option update'] = """
    type: command
    short-summary: Update an option from an existing content key policy.
    examples:
        - name: Update an existing content-key-policy by adding an alternate token key to an existing option.
          text: >
            az ams content-key-policy option update -n contentKeyPolicyName -g resourceGroup -a amsAccount --policy-option-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --add-alt-token-key tokenKey --add-alt-token-key-type Symmetric
"""

helps['ams job'] = """
    type: group
    short-summary: Manage jobs for a transform.
"""

helps['ams job create'] = """
    type: command
    short-summary: Create and start a job.
"""

helps['ams job update'] = """
    type: command
    short-summary: Update an existing job.
"""

helps['ams job list'] = """
    type: command
    short-summary: List all the jobs of a transform within an Azure Media Services account.
    examples:
        - name: List all the jobs of a transform with 'Normal' priority by name.
          text: >
            az ams job list -a amsAccount -g resourceGroup -t transformName --query [?priority=='Normal'].{jobName:name}
        - name: List all the jobs of a transform by name and input.
          text: >
            az ams job list -a amsAccount -g resourceGroup -t transformName --query [].{jobName:name,jobInput:input}
"""

helps['ams job show'] = """
    type: command
    short-summary: Show the details of a job.
"""

helps['ams job delete'] = """
    type: command
    short-summary: Delete a job.
"""

helps['ams job cancel'] = """
    type: command
    short-summary: Cancel a job.
"""

helps['ams streaming-locator'] = """
    type: group
    short-summary: Manage streaming locators for an Azure Media Services account.
"""

helps['ams streaming-locator create'] = """
    type: command
    short-summary: Create a streaming locator.
"""

helps['ams streaming-locator list'] = """
    type: command
    short-summary: List all the streaming locators within an Azure Media Services account.
"""

helps['ams streaming-locator show'] = """
    type: command
    short-summary: Show the details of a streaming locator.
"""

helps['ams streaming-locator get-paths'] = """
    type: command
    short-summary: List paths supported by a streaming locator.
"""

helps['ams streaming-locator list-content-keys'] = """
    type: command
    short-summary: List content keys used by a streaming locator.
"""

helps['ams streaming-policy'] = """
    type: group
    short-summary: Manage streaming policies for an Azure Media Services account.
"""

helps['ams streaming-policy create'] = """
    type: command
    short-summary: Create a streaming policy.
"""

helps['ams streaming-policy list'] = """
    type: command
    short-summary: List all the streaming policies within an Azure Media Services account.
"""

helps['ams streaming-policy show'] = """
    type: command
    short-summary: Show the details of a streaming policy.
"""

helps['ams streaming-endpoint'] = """
    type: group
    short-summary: Manage streaming endpoints for an Azure Media Service account.
"""

helps['ams streaming-endpoint start'] = """
    type: command
    short-summary: Start a streaming endpoint.
"""

helps['ams streaming-endpoint stop'] = """
    type: command
    short-summary: Stop a streaming endpoint.
"""

helps['ams streaming-endpoint list'] = """
    type: command
    short-summary: List all the streaming endpoints within an Azure Media Services account.
"""

helps['ams streaming-endpoint create'] = """
    type: command
    short-summary: Create a streaming endpoint.
"""

helps['ams streaming-endpoint wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the streaming endpoint is met.
    examples:
        - name: Place the CLI in a waiting state until the streaming endpoint is created.
          text: az ams streaming-endpoint wait -g MyResourceGroup -a MyAmsAccount -n MyStreamingEndpoint --created
"""

helps['ams streaming-endpoint akamai'] = """
    type: group
    short-summary: Manage AkamaiAccessControl objects to be used on streaming endpoints.
"""

helps['ams streaming-endpoint akamai add'] = """
    type: command
    short-summary: Add an AkamaiAccessControl to an existing streaming endpoint.
"""

helps['ams streaming-endpoint show'] = """
    type: command
    short-summary: Show the details of a streaming endpoint.
"""

helps['ams streaming-endpoint delete'] = """
    type: command
    short-summary: Delete a streaming endpoint.
"""

helps['ams streaming-endpoint akamai remove'] = """
    type: command
    short-summary: Remove an AkamaiAccessControl from an existing streaming endpoint.
"""

helps['ams streaming-endpoint scale'] = """
    type: command
    short-summary: Set the scale of a streaming endpoint.
"""

helps['ams streaming-endpoint update'] = """
    type: command
    short-summary: Update the details of a streaming endpoint.
"""

helps['ams live-event'] = """
    type: group
    short-summary: Manage live events for an Azure Media Service account.
"""

helps['ams live-event create'] = """
    type: command
    short-summary: Create a live event.
"""

helps['ams live-event start'] = """
    type: command
    short-summary: Start a live event.
"""

helps['ams live-event show'] = """
    type: command
    short-summary: Show the details of a live event.
"""

helps['ams live-event list'] = """
    type: command
    short-summary: List all the live events of an Azure Media Services account.
    examples:
        - name: List all the live events by name and resourceState quickly.
          text: >
            az ams live-event list -a amsAccount -g resourceGroup --query [].{liveEventName:name,state:resourceState}
"""

helps['ams live-event delete'] = """
    type: command
    short-summary: Delete a live event.
"""

helps['ams live-event stop'] = """
    type: command
    short-summary: Stop a live event.
"""

helps['ams live-event reset'] = """
    type: command
    short-summary: Reset a live event.
"""

helps['ams live-event update'] = """
    type: command
    short-summary: Update the details of a live event.
    examples:
        - name: Set a new allowed IP address and remove an existing IP address at index '0'.
          text: >
            az ams live-event update -a amsAccount -g resourceGroup -n liveEventName --remove input.accessControl.ip.allow 0 --add input.accessControl.ip.allow 1.2.3.4/22
        - name: Clear existing IP addresses and set new ones.
          text: >
            az ams live-event update -a amsAccount -g resourceGroup -n liveEventName --ips 1.2.3.4/22 5.6.7.8/30

"""

helps['ams live-event wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the live event is met.
    examples:
        - name: Place the CLI in a waiting state until the live event is created.
          text: az ams live-event wait -g MyResourceGroup -a MyAmsAccount -n MyLiveEvent --created
"""

helps['ams live-output'] = """
    type: group
    short-summary: Manage live outputs for an Azure Media Service account.
"""

helps['ams live-output create'] = """
    type: command
    short-summary: Create a live output.
"""

helps['ams live-output show'] = """
    type: command
    short-summary: Show the details of a live output.
"""

helps['ams live-output list'] = """
    type: command
    short-summary: List all the live outputs in a live event.
"""

helps['ams live-output delete'] = """
    type: command
    short-summary: Delete a live output.
"""

helps['ams account-filter show'] = """
    type: command
    short-summary: Show the details of an account filter.
"""

helps['ams account-filter list'] = """
    type: command
    short-summary: List all the account filters of an Azure Media Services account.
"""

helps['ams account-filter create'] = """
    type: command
    short-summary: Create an account filter.
    examples:
        - name: Create an asset filter with filter track selections.
          text: >
            az ams account-filter create -a amsAccount -g resourceGroup -n filterName --force-end-timestamp=False --end-timestamp 200000 --start-timestamp 100000 --live-backoff-duration 60 --presentation-window-duration 600000 --timescale 1000 --first-quality 720 --tracks @C:\\tracks.json
"""

helps['ams account-filter update'] = """
    type: command
    short-summary: Update the details of an account filter.
"""

helps['ams account-filter delete'] = """
    type: command
    short-summary: Delete an account filter.
"""

helps['ams account mru'] = """
    type: group
    short-summary: Manage media reserved units for an Azure Media Services account.
"""

helps['ams account mru set'] = """
    type: command
    short-summary: Set the type and number of media reserved units for an Azure Media Services account.
"""

helps['ams account mru show'] = """
    type: command
    short-summary: Show the details of media reserved units for an Azure Media Services account.
"""

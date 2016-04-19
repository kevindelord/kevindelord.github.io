---
layout:     post
title:      Upload an app to iTunesConnect
summary:    Build and upload an app binary to iTunesConnect with Application Loader.
---

Uploading a new app to iTunesConnect is much more complicated than it seems.

Most of time something wrong happen like bad certificate, missing swift content, bitcode issues, etc.

This page explains different tips and tricks about it.

#### Important notice

This article has been written as the earliest versions of Xcode were buggy when releasing Swift apps. :rage:

A workout around was to use Application Loader instead. 

This solution might be complicated or even deprecated with the newest/next version of Xcode.

## Working flow

Here is a step-by-step quick list to upload a binary to iTunesConnect:

1. Make sure you locally have the latest code, the right **provisioning profile** and **distribution certificate**.

2. Make sure iTunesConnect is well configured regarding the app version. Basically your app version (1.0.1) should match the one set on iTunesConnect.

3. **Build and archive** the LIVE target locally on your computer using Xcode.

4. In the **Organizer**, you need to **export** the binary "for iOS App Store Deployment".

5. Open the **Application Loader** and sign in with a correct account.

6. **Choose to upload** a binary and go through the process (be careful regarding the **bitcode**).

7. Finally upload the **.ipa** and **.dSYM.zip** to Hockey.

8. Add a git tag, it looks cool on GitHub :wink:

## Developer accounts

To develop on iOS, to build an app on a physical device and to release an app on the official store, you always need a developer account.

You also need this account to be configured in Xcode and in Application Loader.

### In Xcode

On Xcode you need an account that is within a **Development Team** accessing the original (paid) developer account that can release an app, also called _Apple Developer Program_.

Once you have the right credentials, open the preferences panel, tab _Accounts_ and add the account.

After that you will be able to set the **team** (in the general tab) for the LIVE target you will need to release.

![_config.yml]({{ site.baseurl }}/images/itunesconnect/team.png)

## Provisioning profile and distribution certificate

An application distributed through the AppStore must be linked to a valid developer account.

This means that to be able to locally build and archive an app for the customer, you need few things:

- The correct **distribution certificate** with the private key inside it.
- A valid **provisioning profile** matching the distribution certificate.

You can create or renew the profile on the Apple developer portal using an account that has the right access.

## Archive a new binary

If you have access to the correct distribution certificate, provisioning profile, development team and an account to upload the binary, then you can proceed to the build and archive phase.

First select the LIVE target and a plugged-in device or the "Generic iOS Device":

![_config.yml]({{ site.baseurl }}/images/itunesconnect/select_device.png)
 
Then open then **Product** panel and hit the **Archive** button.

![_config.yml]({{ site.baseurl }}/images/itunesconnect/archive.png)
 
Xcode will take a while to build and archive your app, once done it will open the **Organizer** window.

## Export for iOS App Store Deployment

Within this view, hit the **Export** button and select **Save for iOS App Store Deployment**:

![_config.yml]({{ site.baseurl }}/images/itunesconnect/export.png)

Choose the correct **Development Team**:

![_config.yml]({{ site.baseurl }}/images/itunesconnect/dev_team.png)

And finally reach the final summary view:

![_config.yml]({{ site.baseurl }}/images/itunesconnect/summary.png)

### Include bitcode

As highlighted in the previous screenshot, be careful with the **Include bitcode** checkbox.

If your project/target has bitcode enabled then make sure to include it in the exported binary.

If you include it but your target does not, iTunesConnect will reject the binary.

## Upload to iTunesConnect

Technically you could upload a binary to iTunesConnect directly from Xcode using the Organizer window.

Sadly, it seems quite buggy at the moment, using the [Application Loader](https://itunesconnect.apple.com/docs/UsingApplicationLoader.pdf) seems to be a better option.

### Using Application Loader

#### Login

To upload a binary to iTunesConnect you need a specific account that has the rights to upload binaries.

After a successful login within the _Application Loader_, you should arrive to this screen:

![_config.yml]({{ site.baseurl }}/images/itunesconnect/applicationloader.png)

#### Upload

Within Application Loader, click on **Deliver Your App**, **Choose** and then select the binary to upload.

A dedicated view should appear showing information about the selected build. Check if everything is fine and hit the **Next** button. 

![_config.yml]({{ site.baseurl }}/images/itunesconnect/final.png)

After this view, the upload to iTunesConnect will start. You will get notified on success or failure.

It takes usually a while for iTC to find problems into your binary.

That's why you should take a break and come back after 10 minutes to verify on iTunesConnect if the build has been successfully uploaded or not.

:palm_tree::innocent::palm_tree:

## Upload to Hockey

In order to manually upload the new version to Hockey, you need two things:

- The **.ipa binary** previously generated. 
- The **.dSYM.zip** file related to the binary.

Once you have both files, please see how you can [manually upload a new app version to hockey](/2016/04/19/configure-hockeyapp).

### Find the dSYM file

Back on the **Organizer** window, select the exported archive, right click and hit the button **Show in finder**.

![_config.yml]({{ site.baseurl }}/images/itunesconnect/show_in_finder.png)

Then right click again and select **Show Package Contents**.

![_config.yml]({{ site.baseurl }}/images/itunesconnect/packages.png)

Within the **dSYMs** folder you should find a .dSYM file with a name like this: _TARGET_NAME.app.dSYM_

![_config.yml]({{ site.baseurl }}/images/itunesconnect/dsym.png)

Copy this file to your Desktop and compress it.

In the end you should have the required _TARGET_NAME.app**.dSYM.zip**_ file.

## Git maintenance

### Remove old branches

Do not hesitate to remove _useless_ or _merged_ or _deprecated_ branches. They are not useful and are just polluting the git repo. 

### Add a release tag

A small thing everybody not to forget is to add a **git tag** when pushing the app to the store.

It is quite handy to keep track of important releases.

On the terminal, execute the following commands:

{% highlight lineanchors %}
$> git tag -a 1.2 -m "New AppStore release. Add chat feature"
$> git push --tags
{% endhighlight lineanchors %}
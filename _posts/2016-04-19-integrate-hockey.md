---
layout:     post
title:      Integrate Hockey SDK
summary:    Configure a new app in hockey with a specific naming convention and other tips.
---

This page explains how to configure a new app in hockey with a specific naming convention and other tips.

## Application naming convention

The naming convention on Hockey for the iOS apps is the same one that the one on Jenkins.

The apps should use the **target name** to clearly identify what kind of app / configuration / setup it is.

![_config.yml]({{ site.baseurl }}/images/hockey/target_names.png)

## Creating New App

There is two ways to create apps on Hockey: Automatic and Manually.

The second one is a better one as you can be sure that everything is correctly setup.

### Automatic

The idea is to configured a [build job on Jenkins](#) (:construction_worker:) without the App ID and run the process.

Once the build done, the necessary files will be uploaded to Hockey.

If the _App ID_ isn't specified, the app with the _same bundle identifier_ will be updated.

If no existing app has this identifier a new Hockey app will be created. After that you should set the new App ID on Jenkins to avoid further complications.

#### On the Apple Developer Portal

When creating new apps on the Apple Developer Portal, the bundle identifier has to be very specific.

The default naming is `com.myEnterprise.yourProject.releaseType`. For example: com.smartmobilefactory.dr.oetker-verlag.alpha

### Manually

It is also possible to avoid the step were Jenkins push a new version to an unknown Hockey app.

First on the _Hockey Dashboard_, click on **New App**. You should see the following popup.

Click on the small **manually** link.

![_config.yml]({{ site.baseurl }}/images/hockey/manually.jpg)
 
Then you need to specify a **Release Type**, **Title** and **Bundle Identifier**.

![_config.yml]({{ site.baseurl }}/images/hockey/app_type.png)

On **Save** a new Hockey App should be created.

## Hockey App ID

After creating a Hockey App, an **App ID** is generated. Copy/paste this value in the configuration page for the dedicated target on **Jenkins**.

This ID also has to be set in your project. The **info PList files** are a great idea! :thumbsup:

![_config.yml]({{ site.baseurl }}/images/hockey/app_id.png)

## Release Type: Alpha / Beta / Enterprise / Store

The release types on Hockey are not the same you actually use in the Apple Developer Portal or in Xcode.

Nonetheless you could try to be, as much as possible, consistent.

Here is how you could name the builds:

- **Alpha**: for all _Alpha-AdHoc_ builds.
- **Beta**: for all _Beta-AdHoc_ builds.
- **Enterprise**: for all _InHouse_ builds.
- **Store**: just for the _Live-AppStore_.

## Upload a new version

### Automatic

Thanks to the Continuous Integration process, every version built on Jenkins will be uploaded to Hockey.

Every ALPHA, BETA, LIVE, Adhoc or Inhouse builds should appear on Hockey with the **.dSYM.zip** file already there.

As far as this automatic process works you have _nothing_ to do. :bowtie:

### Manually

But if for some reasons you want to locally build and archive a new version of an app, you will also need to upload it to Hockey.

This upload will distribute the new version and let, for example, the beta testers do their job.

To do so, open the dedicated page of the app on [rink.hockeyapp.net](https://rink.hockeyapp.net/manage/dashboard) and hit the big blue **Add Version** button.

![_config.yml]({{ site.baseurl }}/images/hockey/add_version.png)

A popup will appear on your web navigator, drop the **.ipa** file there. It will start the upload process.

Once done, you should be redirected to a new page dedicated to the version of the app you have just uploaded.

On the right side, click on **Upload .dSYM.zip** to upload the related file.

In the end, your view should look like this:

![_config.yml]({{ site.baseurl }}/images/hockey/downloads.png)

If you are not sure how to get this **.dSYM.zip** file, please read [this page](/2016/03/29/upload-to-itunesconnect).

The new version is ready to be distributed and installed on real devices!

## New store version

After releasing an app with **Application Loader** you need to create a new version on Hockey.

But if the _Release Type_ of the app on Hockey is set to _Store_ you can't upload both **.ipa** and **.dSYM.zip** files.

The workaround is to go to **Manage App** and change the **Release Type** to **Enterprise**.

Once everything has been uploaded to both iTunesConnect and Hockey, do not forget to put setting back to **Store**.


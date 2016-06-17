---
layout: post
title: Configure an iOS build job on Jenkins
summary: See how to setup a new iOS build job on jenkins with automatic new releases and push to HockeyApp.
---

This page isn't about Jenkins and how it should be configured.

Nonetheless here is some information about iOS build jobs.

When creating a new job it is sometimes very useful to actually create a job from an already existing one.

And then just configure the fields that need to be.


## Naming

Every build jobs should be named regarding the **target** it is building.

For example:

![_config.yml]({{ site.baseurl }}/images/jenkins/naming.png)

## Poll SCM

This automatically build a new version every time something is pushed to the configured branch.

It should only be activated for the base target, in most the `Project-Alpha-AdHoc`.

![_config.yml]({{ site.baseurl }}/images/jenkins/poll_scm.png)

If you need to build other jobs, do it manually.

## Build Environment

The **resource to manage exclusion** helps you to avoid conflict when building the same project with multiple targets at the same time.

All jobs for the same project should have the same value set.

If so, when scheduling 10 different builds they will be done one by one.

![_config.yml]({{ site.baseurl }}/images/jenkins/resource.png)

## iOS Building

The following screenshot shows the general rule about the build job configuration.
Please note that come configuration change if the target is the base one or not.

![_config.yml]({{ site.baseurl }}/images/jenkins/build_settings.jpg)

### Important

**Increment Build Number** and **Push increment version number to git after build** should only be activated for the _base_ build job.

The **API Token** should be the same one for every project.

The **App ID** is actually the Hockey App ID for the current target.

### Pro Tip

When building a whole new set of versions (`Alpha-AdHoc`, `Beta-InHouse`, etc.) always try to **just build the base job/target first**, and then (when it's done) all the others.

By doing this, you will make sure all new released versions will have the same version number.

## Distribution Certificate and Provisioning Profiles

When you are trying to build jobs related to a target inside a xcode project or workspace, be sure that the **Provisioning Profiles** have been uploaded to Jenkins.

But also that the **Distribution Certificates** that generated those profiles is correctly uploaded too!

![_config.yml]({{ site.baseurl }}/images/jenkins/certificate.jpg)


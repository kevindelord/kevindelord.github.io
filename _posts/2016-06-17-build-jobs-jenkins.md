---
layout: post
title: Configure an iOS build job on Jenkins
summary: See how to setup a new iOS build job on jenkins with automatic new releases and push to HockeyApp.
---

This page isn't about Jenkins and how it should be configured but more about iOS build jobs.

It explains how to setup a job in order to properly build and release a new version of your app on [HockeyApp](https://www.hockeyapp.net).

The most relevant fields are explained and detailed with screenshots.

## Naming

First of all, the name of the job should be very explicit. It should detail exactly _what_ it is and what it builds.

A good practice is to use the **target name** it is actually building.

More information about correct target naming on this article: [Xcode Project Configuration](http://kevindelord.io/2016/06/08/project-configuration/).

For example, with a project called `Dr.Oetker-Verlag` the build jobs on Jenkins would be named:

![_config.yml]({{ site.baseurl }}/images/jenkins/naming.png)

## SCM: Source Code Management

Jenkins allows you to pull and build project using different source code management such as [Git](https://git-scm.com), [Mercurial](https://www.mercurial-scm.org), etc.

In most case you need to specify two things:

- **Repository URL**: The url pointing to your source code.
- **Branch Specifier**: The branch to take the code from in order to build a new app version.

![_config.yml]({{ site.baseurl }}/images/jenkins/git.png)

## Build Triggers

There are multiple ways to automatically trigger a build process.

The most common ones are:

- `Build after other projects are built`

This will start a new build when another one has _successfully_ built.

- `Build periodically`

This will regurlarly trigger a new build at a constant interval of time.

- `Poll SCM`

This automatically build a new version every time something is pushed to the configured branch.

this option should only be activated for the base target, in most the `Project-Alpha-AdHoc`. If you need to build other jobs, do it manually.


![_config.yml]({{ site.baseurl }}/images/jenkins/poll_scm.png)


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


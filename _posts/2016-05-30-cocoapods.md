---
layout: post
title: Cocoapods
summary: How to setup and configure Cocoapods on your computer and for your project.
---

## Installation and update

If you need to install or update cocoapods on a machine, please refer to the [official documentation](https://guides.cocoapods.org/using/getting-started.html).
Nonetheless, here is the most useful command line:

{% highlight swift lineanchors %}
$> sudo gem install cocoapods
{% endhighlight lineanchors %}

## Integration

First you need to create a simple file named **Podfile**.
Here is an example for the BDG project containing two targets: `DBG-Alpha-InHouse` and `DBG-Beta-InHouse`:

{% highlight ruby lineanchors %}
$> cat Podfile

source 'https://github.com/CocoaPods/Specs.git'

platform :ios, '8.0'
use_frameworks!

def corePods
	pod 'DKHelper', '~> 2.1.4'
	pod 'UIImage+Autoresize', '~> 1.1.1'
	pod 'HockeySDK', '~> 3.8.6'
	pod 'Appirater', '~> 2.0.5'
end
target 'DBG-Alpha-InHouse' do
	corePods
end

target 'DBG-Beta-InHouse' do
	corePods
end
{% endhighlight lineanchors %}

Make sure that the platform version written (here '`8.0`') is the same as the minimum deployment target set in your project.
After this, run the command `pod install. It will download the libraries and integrate them into your project by creating a Xcode workspace.

{% highlight swift lineanchors %}
$> pod install
{% endhighlight lineanchors %}

Once done, be sure to always open and use the generated **.xworkspace** in xcode!

## Pod versioning

As you can see in the previous example, the installed pods are followed by `'~> 3.8.5'.
This is very important as it controls which version of the library your code is using, but most important, which is version it is ready to use.
If you do _not_ specify a version, Cocoapods will install the latest one.
This could be a very big problem if some big changes occurred in the library and your code is not ready for them.
The Continuous Integration process could fail and, unless you know the version you need, you might never be able to release a new beta to the customers... oops.
Read the official documentation to learn more about [using cocoapods](https://guides.cocoapods.org/using/using-cocoapods.html) and the [Podfile](https://guides.cocoapods.org/using/the-podfile.html).

## Git ignore

Cocoapods generate a folder called **Pods** containing all source code for every single library.
This does not need to be either committed or pushed to your git server.
To avoid this add `Pods` to your **.gitignore**.

TODO
We recommend against adding the Pods directory to your .gitignore.
However you should judge for yourself, the pros and cons are mentioned at:

https://guides.cocoapods.org/using/using-cocoapods.html#should-i-check-the-pods-directory-into-source-control

## Outdated Pods

A small note about pods. While maintaining an app, bugs often comes from outdated libraries.

When starting to code or debug make sure to run `pod outdated` to see which ones are deprecated or have a new version.

When updating some libraries take care of any breaking changes, new warnings, etc. You should **understand** what's new in the update.

{% highlight swift lineanchors %}
$> pod outdated
{% endhighlight lineanchors %}

## Adding Swift pods

### Pods as frameworks

Through Cocoapods, the Swift libraries must be integrated as **frameworks**.
To do so, make sure to add the following into your **Podfile**:

{% highlight swift lineanchors %}
use_frameworks!
{% endhighlight lineanchors %}

Be careful, once this is done not only the Swift libraries but also the Obj-C ones will be integrated as frameworks.
You will need to import them using the swift import `@import MyLibrary` in your files instead of `#import "MyLibrary.h` in the bridging header file.

### Code signing issue

When integrating the pods as frameworks, Jenkins will build the pods and expect provisioning profile for each pod.
Of course, this is not a normal behaviour and you might get an error something like this one:

{% highlight ruby lineanchors %}
=== CLEAN TARGET Pods-Xxxxxxxxx OF PROJECT Pods WITH CONFIGURATION Release ===

Check dependencies
[BEROR]Code Sign error: No code signing identities found: No valid signing identities (i.e. certificate and private key pair) matching the team ID “(null)” were found.
[BEROR]CodeSign error: code signing is required for product type 'Framework' in SDK 'iOS 8.1'
{% endhighlight lineanchors %}

This error is related to how CocoaPods expects code signing configurations for **frameworks**.
You should add the following script as a Post script to your **Podfile**:

{% highlight ruby lineanchors %}
post_install do |installer|
	installer.pods_project.targets.each do |target|
		if target.name.include?("Pods-")
			require 'fileutils'
			FileUtils.cp_r('Pods/Target Support Files/' + target.name + '/' + target.name + '-acknowledgements.plist',
			'Resources/Settings.bundle/Pods-acknowledgements.plist', :remove_destination => true)
		end
	end
end
{% endhighlight lineanchors %}

## Pods Acknowledgements

Whenever you run `pod install, Cocoapods will automatically generate an acknowledgements file containing the license of all used libraries.
By respect for the original developer(s), it is very much appreciated to grant them credits and let the final users know you are using their code.
To do so, add a **Settings.bundle** to your project and add the following to your **Podfile**:

{% highlight ruby lineanchors %}
post_install do |installer|
	installer.pods_project.targets.each do |target|
		if target.name.include?("Pods-")
			require 'fileutils'
			FileUtils.cp_r('Pods/Target Support Files/' + target.name + '/' + target.name + '-acknowledgements.plist',
			'Resources/Settings.bundle/Pods-acknowledgements.plist', :remove_destination => true)
		end
	end
end
{% endhighlight lineanchors %}

To learn more about this, see this [official page](https://github.com/CocoaPods/CocoaPods/wiki/Acknowledgements).

Now open the Settings.bundle in Xcode and make sure the Root.plist file is configured like this:

{% highlight swift lineanchors %}
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PreferenceSpecifiers</key>
	<array>
		<dict>
			<key>File</key>
			<string>Pods-acknowledgements</string>
			<key>Title</key>
			<string>Acknowledgements</string>
			<key>Type</key>
			<string>PSChildPaneSpecifier</string>
		</dict>
	</array>
	<key>StringsTable</key>
	<string>Root</string>
</dict>
</plist>
{% endhighlight lineanchors %}

Of course depending on your project, you can/should add other entries in this plist to let the final user configures the app.

**Remark**: Do not forget to `pod install` again :]

Thanks for reading !

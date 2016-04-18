---
layout:     post
title:      App Transport Security
summary:    How to configure security exceptions for HTTP connections.
---

iOS 9 has a new security feature that improve how an app can access the web or… how the web can access an app and the device itself.

## What is it

From the [official documentation](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) about the _App Transport Security_ (ATS):

> It improves the privacy and data integrity of connections between an app and web services by enforcing additional security requirements for HTTP-based networking requests. [...] Attempts to connect using insecure HTTP fail. Furthermore, HTTPS requests must use best practices for secure communications.

This means that an iOS device will automatically block connections to a server when its SSL, TLS certificates and configuration are either outdated or insecure.

Obviously some backend / API / web views related bugs you could get from now on, might be due to those changes. :frowning:

## What To Do

To make sure your app can still access its _outdated and insecure_ backend and APIs, you need to add exceptions into your Plists files.

In few words, just tell your device to ignore the fact that those backends are dangerous.

Once you know which backends are insecure, you have to specify their domain names under the `NSAppTransportSecurity` of the Plist files.

For example, if your api on the machine behind `my.api.domain.com` is insecure, add and adapt the following at the end of every info.plist of your project (for each target):

{% highlight swift %}
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSExceptionDomains</key>
    <dict>
        <key>my.api.domain.com</key>
        <dict>
            <key>NSIncludesSubdomains</key>
            <true/>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <true/>
            <key>NSExceptionRequiresForwardSecrecy</key>
            <false/>
        </dict>
    </dict>
</dict>
{% endhighlight %}

#### Important

If the API is on an updated server, you do not need to add any exception on your PList files.

### Exception keys

List of keys and description of server-specific exceptions to your app’s overall intended network behavior:

| Key | Type | Description |
|:----|:-----|:------------|
| NSIncludesSubdomains | Boolean | Apply the ATS exceptions to all subdomains. |
| NSExceptionAllowsInsecureHTTPLoads | Boolean | Allows insecure HTTP loads. |
| NSExceptionRequiresForwardSecrecy | Boolean | Override the requirement that a server support forward secrecy or not. |
| NSExceptionMinimumTLSVersion | String | Minimum TLS version supported. |

#### Third Parties

It is also possible configure exceptions of a domain whose security attributes you do not control (i.e.: third party libraries).

| Key | Type |
|:----|:-----|
| NSThirdPartyExceptionAllowsInsecureHTTPLoads | Boolean |
| NSThirdPartyExceptionRequiresForwardSecrecy | Boolean |
| NSThirdPartyExceptionMinimumTLSVersion | String |

#### Important

Once again, only set what you _need_, make sure you do not disable any security feature without reason.

## What *NOT* to do

You could also disable the complete ATS feature and let the app access every single insecure URLs.

Of course this easy dirty solution is not the right one, but in case of despair it might help quite a lot.

{% highlight swift %}
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
{% endhighlight %}

## How to know what exceptions do you need?

If you do not know which exceptions you really need, there is an easy way to test the backend your app will access.

Open the terminal and use the following command: 

	$> nscurl --ats-diagnostics https://base.url.of.my.api.com

And for more information:

	$> nscurl --ats-diagnostics --verbose https://base.url.of.my.api.com

All kind of tests will be done: with or without SSL, different TLS versions, etc.

The result displayed should be able to help you setting for each domain the exceptions you need. :sunglasses:

## External Links

* [Official ATS documentation](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33)
* [iOS 9 release notes](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html)
* [Very nice Steven Peterson post](http://ste.vn/2015/06/10/configuring-app-transport-security-ios-9-osx-10-11)

On StackOverFlow [this thread](http://stackoverflow.com/questions/30739473/nsurlsession-nsurlconnection-http-load-failed-on-ios-9) is the most valuable one, its second answer is great explanation while the third one tells you _what_ to do (while being security-safe).

---
layout:     post
title:      Integrate Swiftlint
date:       2015-05-04 14:10:00
summary:    Learn how to set up Swiftlint within an Xcode project.
---

SwiftLint is an experimental tool enforcing Swift style and conventions, loosely based on [GitHub's Swift Style Guide](https://github.com/github/swift-style-guide).
It hooks into Clang and SourceKit to use the AST representation of the source files for more accurate results.

Depending on your code quality, integrating SwiftLint and update the code to satisfy the selected rules might take between 1 and 2 hours. 

## Requirements

This only works for projects on Swift 2.0 and newer.

Obj-C project and older versions of swift are not supported.

## SwiftLint on your computer

### Install

First of all, you need to install the SwiftLint framework on your machine:

{% highlight lineanchors %}
$> brew update
$> brew install swiftlint
{% endhighlight %}

### Update

If you already have it and it's time to update your local configuration, use the following:

{% highlight lineanchors %}
$> brew update
$> brew upgrade swiftlint
{% endhighlight %}

### Specific version

If for some reason you updated the framework to a new version not yet supported by our infrastructure, you can simply configure brew and set the right one.

For example, to set the version back to 0.4.0:

{% highlight lineanchors %}
$> brew switch swiftlint 0.4.0
{% endhighlight %}

### Current version

If you want to check which is the current version of Swiftlint installed on your computer, use the following:

{% highlight lineanchors %}
$> swiftlint version
{% endhighlight %}

## Integrate SwiftLint into a project

To integrate the framework you need two things:

  * A configuration file.
  * A new Run Script Phase of each of your targets.

### Create/Update the configuration file

The configuration file actually describe which rules should be used by the framework when checking the code.

A custom version should be used to satisfy both SwiftLint and this [Swift Style Guide](https://github.com/kevindelord/swift-style-guide).
To do so execute the following command line (while being in the project folder):

{% highlight lineanchors %}
$> curl https://raw.githubusercontent.com/kevindelord/swift-style-guide/master/.swiftlint.yml > .swiftlint.yml   
{% endhighlight lineanchors %}

NB: If the project already integrates Swiftlint, the .swiftlint.yml should be in the git repo. A simple git pull will fetch it for you.    

### Setup Xcode

To integrate SwiftLint into a Xcode project, you need to create a new *Run Script Phase*.

It should be configured like this:

{% highlight lineanchors %}
if which swiftlint >/dev/null; then
  swiftlint
else
  echo "SwiftLint does not exist, download from https://github.com/realm/SwiftLint"
fi
{% endhighlight lineanchors %}

Whick looks like this on Xcode:

![_config.yml]({{ site.baseurl }}/images/swiftlint/runscript.png)

After building the code, Xcode should now displays errors and warnings like this:

![_config.yml]({{ site.baseurl }}/images/swiftlint/warning_sample.png)

## Active SwiftLint rules 

Enabled Rules
Name	
Reason
comma
k,v >> k, v
file_length	max number of lines per file
force_cast	as!
force_try	try!
function_body_length	max length of function body
leading_whitespace	empty lines with whitespaces only
legacy_constructor	e.g CGPointMake(...) >>> CGPoint(x: ..., y: ...)
line_length	max length of a line
opening_brace	[].map(){ ... } >>> [].map() { ... }
operator_function_whitespace	func  thing () {...} >>> func thing() {...}
return_arrow_whitespace	func thing()->Bool >>> func thing() -> Bool
statement_position	 }else if { >>> } else if {
trailing_newline	new line at the end of a file
trailing_semicolon	no ;
trailing_whitespace	no trailing whitespace
type_body_length	max body length
type_name 	types should start with a capital letter
valid_docs 	docs should match the method signature
variable_name	variable names should only contain alphabetic characters
variable_name_min_length	variables should have a 3 letter minimum name
Disabled Rules
Name	Reason
nesting	This one tries to control the level of 'nesting'. Problem the types should have just 1 level deep, meaning a struct can't contain another struct.
colon	This rule forces the colon to be 'attached' to the variable `let abc: Void`; which is against our style guide.
control_statement	This rule asks for `if` without rounded brackets; which is completely against our style guide.
todo	TODOs should not be a warning. One can add TODO but must create a related ticket on JIRA.


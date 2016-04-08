---
layout:     post
title:      Integrate Swiftlint
summary:    Learn how to install Swiftlint on your computer and configure an existing Xcode project.
---

SwiftLint is an experimental tool enforcing Swift style and conventions, loosely based on [GitHub's Swift Style Guide](https://github.com/github/swift-style-guide).
It hooks into Clang and SourceKit to use the AST representation of the source files for more accurate results.

Depending on your code quality, integrating SwiftLint and update the code to satisfy the selected rules might take between 1 and 2 hours. 

## Requirements

This only works for projects on Swift 2.0 and newer.

Obj-C projects and older versions of Swift are not supported.

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

If for some reason you updated the framework to a new version not yet supported by your infrastructure, you can `switch` to the right one.

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

  * A configuration file: `.swiftlint.yml`
  * A new Run Script Phase of each of your targets.

### Create/Update the configuration file

The configuration file describes which rules should be used by the framework when checking the code.

A custom version should be used to satisfy both SwiftLint and this [Swift Style Guide](https://github.com/kevindelord/swift-style-guide).
To do so execute the following command line (while being in the project folder):

{% highlight lineanchors %}
$> curl https://raw.githubusercontent.com/kevindelord/swift-style-guide/master/.swiftlint.yml > .swiftlint.yml   
{% endhighlight lineanchors %}

NB: If the project already integrates Swiftlint, the `.swiftlint.yml` should be in the git repo. A simple git pull will fetch it for you.    

### Setup Xcode

To integrate SwiftLint into an existing Xcode project, you need to create a new `Run Script Phase`.

It should be configured like this:

{% highlight lineanchors %}
if which swiftlint >/dev/null; then
  swiftlint
else
  echo "SwiftLint does not exist, download from https://github.com/realm/SwiftLint"
fi
{% endhighlight lineanchors %}

Which looks like this on Xcode:

![_config.yml]({{ site.baseurl }}/images/swiftlint/runscript.png)

After building the code, Xcode should now displays errors and warnings like this:

![_config.yml]({{ site.baseurl }}/images/swiftlint/warning_sample.png)

## SwiftLint rules

### Check enabled rules

Execute this command to check which rules are enabled or not for your current configuration: 

{% highlight lineanchors %}
$> swiftlint rules
{% endhighlight lineanchors %}

### Rule description

To get more details about one specific rule, such as a description and some examples, execute the following command:

{% highlight lineanchors %}
$> swiftlint rules force_cast
{% endhighlight lineanchors %}

### List of rules

| Name  | Description |
|:------|:------------|
| closing_brace               | Closing brace with closing parenthesis should not have any whitespaces in the middle. |
| colon                       | Colons should be next to the identifier when specifying a type. |
| comma                       | There should be no space before and one after any comma. |
| conditional_binding_cascade | Repeated `let` statements in conditional binding cascade should be avoided. |
| control_statement           | if,for,while,do statements shouldn't wrap their conditionals in parentheses. |
| custom_rules                | Create custom rules by providing a regex string. Optionally specify what syntax kinds to match against, the severity level, and what message to display. |
| cyclomatic_complexity       | Complexity of function bodies should be limited. |
| empty_count                 | Prefer checking `isEmpty` over comparing `count` to zero. |
| file_length                 | Files should not span too many lines. |
| force_cast                  | Force casts should be avoided. |
| force_try                   | Force tries should be avoided. |
| force_unwrapping            | Force unwrapping should be avoided. |
| function_body_length        | Functions bodies should not span too many lines. |
| function_parameter_count    | Number of function parameters should be low. |
| leading_whitespace          | Files should not contain leading whitespace. |
| legacy_constant             | Struct-scoped constants are preferred over legacy global constants. |
| legacy_constructor          | Swift constructors are preferred over legacy convenience functions. |
| line_length                 | Lines should not span too many characters. |
| missing_docs                | Public declarations should be documented. |
| nesting                     | Types should be nested at most 1 level deep, and statements should be nested at most 5 levels deep. |
| opening_brace               | Opening braces should be preceded by a single space and on the same line as the declaration. |
| operator_whitespace         | Operators should be surrounded by a single whitespace when defining them. |
| return_arrow_whitespace     | Return arrow and return type should be separated by a single space or on a separate line.|
| statement_position          | Else and catch should be on the same line, one space after the previous declaration. |
| todo                        | TODOs and FIXMEs should be avoided. |
| trailing_newline            | Files should have a single trailing newline. |
| trailing_semicolon          | Lines should not have trailing semicolons. |
| trailing_whitespace         | Lines should not have trailing whitespace. |
| type_body_length            | Type bodies should not span too many lines. |
| type_name                   | Type name should only contain alphanumeric characters, start with an uppercase character and span between 3 and 40 characters in length. |
| valid_docs                  | Documented declarations should be valid. |
| variable_name               | Variable names should only contain alphanumeric characters and start with a lowercase character or should only contain capital letters. In an exception to the above, variable names may start with a capital letter when they are declared static and immutable. Variable names should not be too long or too short. |

Enjoy coding with Swiftlint :]

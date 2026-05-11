---
author: tracetronicGmbH
created: 2026-04-13
description: test.guide 用户文档
published: 2026-04-13
source: "https://testguide.one-cx.cn/help-docs/#\\_how_do_i_set_up_a_q_gate_staging"
tags:
- clippings
title: test.guide user documentation
---

**test.guide** connects test execution and management.
\## 1 Introduction

**test.guide** is a centralized application for the supervision, analysis and follow-up processing of test procedures, which has been specially developed for use in the automotive sector. It significantly facilitates the management of test resources. At the same time, it encourages cross-role cooperation, thereby closing the gap between test execution and test management.

## 1.1. Release Notes

Information on the latest changes to the product can be found at:

- [Release Notes](https://testguide.one-cx.cn/changelog-docs/index.eng.html)
- [Third-Party Software Licenses](https://testguide.one-cx.cn/licenses)

## 1.2. Installing

See the [Operations Manual](https://testguide.one-cx.cn/help-docs/operations_manual.pdf) which is included in the *release zip* in the `/doc` directory.

### 1.2.1. System view

The following system view provides an initial overview of the most important connected subsystems with their interfaces.

<figure>
<img
src="test.guide%20user%20documentation-media/f3967e9ae913e63dd5fcb64377e9256fff55acb9.png"
alt="12b57bbe8a787535056f0aedda4e2834_MD5" />
<figcaption
aria-hidden="true">12b57bbe8a787535056f0aedda4e2834_MD5</figcaption>
</figure>

SystemviewInterfaces

## 1.3. Key modules

This section briefly describes the key modules in **test.guide**.

### 1.3.1. Test report management

#### 1.3.1.1. Project-specific management, analysis and visualization of arbitrary test reports and result data

Test execution in development projects leads to the accumulation of various reports and data. Test automation intensifies this, producing very high numbers of test executions, which are distributed over several users and test environments.

#### 1.3.1.2. Area of Application

**test.guide** is a centralized database application, flexibly deployable in different development and test environments. It has been developed specifically for use in the automotive area and provides the capability to manage, view and analyze test executions and results via an intuitive, web-based interface.

#### 1.3.1.3. Usage Scenarios

<figure>
<img
src="test.guide%20user%20documentation-media/5796d38859e9b780e46cccc2e51f94e3ff812c76.png"
alt="a2bf57e99979099ddd282ac9fe543ed4_MD5" />
<figcaption
aria-hidden="true">a2bf57e99979099ddd282ac9fe543ed4_MD5</figcaption>
</figure>

IntroductionTestReportManagementFeatures

#### 1.3.1.4. Functionality

**test.guide** centrally stores test reports and related file-based test data such as log files or images. By capturing all relevant meta data for every single test execution and providing extensive filtering capabilities, **test.guide** makes analysis of trends or root cause analysis of test failures a breeze.

In order to import test reports of any test execution system, **test.guide** provides an [ASAM ATX](https://www.asam.net/standards/detail/atx/) compliant interface and ready-to-use adapters for the most common test report formats.

The user interface is fully browser-based and supports using **test.guide** on various user devices such as notebooks, smartphones and tablets.

### 1.3.2. Test case coverage

#### 1.3.2.1. Area of application (Just "cover" everything...)

The test case coverage module provides features to analyze test case executions regarding scopes, variants and requirements.

#### 1.3.2.2. Usage Scenarios

<figure>
<img
src="test.guide%20user%20documentation-media/2468ddbbd1ea3ce19852abbd1d4388980c136bce.png"
alt="80c01d87d3191578837f6c9be07f9da8_MD5" />
<figcaption
aria-hidden="true">80c01d87d3191578837f6c9be07f9da8_MD5</figcaption>
</figure>

TestCaseCoverageQuestion

#### 1.3.2.3. Functionality

<figure>
<img
src="test.guide%20user%20documentation-media/249e51e44a7e30565c0b64f9fcaa86992e7268b2.png"
alt="fa738ac96c0bdaad396f5decf894fcf9_MD5" />
<figcaption
aria-hidden="true">fa738ac96c0bdaad396f5decf894fcf9_MD5</figcaption>
</figure>

TestCaseCoverageWorkflow

### 1.3.3. Monitoring

#### 1.3.3.1. Area of application

The monitoring module continuously collects status and health data of the test benches. From this data, **test.guide** provides an overview about the complete test environment's state and allows to relate test results with test bench data. Furthermore test benches observed by the monitoring can be used for automated test execution distribution.

<figure>
<img
src="test.guide%20user%20documentation-media/a477518bcf9be13dfe6f69635e87b814c0bb655d.png"
alt="f5d81d6ca01da354d89d695242344c6c_MD5" />
<figcaption
aria-hidden="true">f5d81d6ca01da354d89d695242344c6c_MD5</figcaption>
</figure>

MonitoringOverview

#### 1.3.3.2. Usage Scenarios

Monitoring provides answers to the following questions:

- Are all test benches available?
- Which test bench is currently showing problems?
- Which tests are currently running on which test benches?
- How are the test benches currently configured?
- How are the test benches working to capacity?

#### 1.3.3.3. Functionality

On each test bench, a small software called the **ResourceAdapter** is executed. It transfers the nodes vital data, test executions and configurations to the central **test.guide** server, where the data is aggregated and related to test case executions.

The **ResourceAdapter** can also be extended via plug-ins, e.g. to capture specific test bench data.

## 2 Using

**test.guide** provides multi-project support. If multiple projects exist, you can switch to another project at the top of the navigation. The navigation also is used to access the different features of **test.guide**.This chapter aims to provide an overview on these features and how to use them.

If you want to use German language, just change the locale at the bottom of the navigation.lightbulb_2

## 2.1. Using the test report management

The main requirement of our customers is to analyze and manage their test report data, which is usually very extensive. Therefore, the *Test report management* section can be used. This section provides a lot of different views to your test reports:

- *Project statistics*: This view provides high level information about test cases and an overview on the project progress. You can have a look at the verdict distribution and some meta information about the uploads.
- *Test plans*: You can use this view if you are interested in the test suites contained in your test reports.
- *Report filter*: The report filter contains the key features of this section.
- *Import ATX*: This view allows you to manually upload test reports.
- *History*: Here you can see a list of the latest uploads.
- *Runtime analysis*: In this view you can manage analyses which examine test case executions by their runtime.

### 2.1.1. Basics of the test report management

#### 2.1.1.1. Which test report formats are supported?

**test.guide** works with the [ASAM ATX](https://www.asam.net/standards/detail/atx/) standardized report format. Furthermore, the application also provides an API (<u style="color: blue;">**X2ATX**</u>) to import data from different formats.

At present, the following formats are supported:

When uploading formats other than ATX, the reports must be contained in a ZIP file.info

If your report format is not listed, there are two solutions available:

- Create a X2ATX plugin matching your very needs.
- (**Recommended**) Make use of the existing JSON plugin by converting the report to the JSON structure defined in its schema.

To download the JSON schema, go to [Import page](https://testguide.one-cx.cn/upload). Select a ZIP file and choose a JSON converter from the drop-down menu. After selecting a plugin, a link for downloading the schema file will appear.

Currently, there are two JSON converters available for the test.guide specific report format: 'JSON Report' and 'JSON2ATX'. The schema provided by the 'JSON Report' converter is more precise and additionally provides support for a wider range of characters within identifiers (see following section about valid identifiers). Therefore it is recommended to use the 'JSON Report' converter.

lightbulb_2

An example of an upload via API can be found in chapter <u style="color: blue;">**Upload via REST API**</u>.info

##### 2.1.1.1.1. Limitations for identifiers

There are certain limitations on the identifiers used for some report elements in test.guide. The following rules apply to test case names, parameter set names, test constant keys, and environment names:

- must contain at least one character
- may contain Unicode characters of the general category 'Letter' (including non-latin letters)
- may contain Unicode characters of the general category 'Number'
- may contain hyphen ("-") and underscore ("\_")

When uploading a report from ecu.test, by default the identifiers will be adjusted automatically to an even more restricted schema, which does not include non-latin characters. Some of the available X2ATX converter will also adjust the reports they convert, following the same rules. For more information on how identifiers are changed, see <u style="color: blue;">Why is the name of my test case in test.guide different than in ecu.test?</u>).

If you want to upload reports with identifiers that contain e.g. non-latin characters or start with a number and do not want them to be adjusted, use the "JSON Report"-converter. This converter does not perform any replacements, but only accepts reports that follow the schema as described above.

When uploading from ecu.test, you can use the option "extendedCharacterSupport" as explained in <u style="color: blue;">Why is the name of my test case in test.guide different than in ecu.test?</u>.

error

#### 2.1.1.2. How do I upload my test reports to test.guide?

You can upload your test reports manually at [Import ATX](https://testguide.one-cx.cn/upload). Select a stand-alone ATX XML file or a ZIP archive containing the report and, optionally, additional arbitrary artifacts like traces, plots, the origin <u style="color: blue;">**TRF report**</u> and many more.

Since a major present-day goal is automation, it is recommended to upload all test reports automatically. Therefore, see <u style="color: blue;">**Upload via REST API**</u>.

##### 2.1.1.2.1. My additional files (like traces, plots, etc.) are very big. How can I speed up the upload process?

There is the possibility to externally upload additional files in advance in order to reduce the size of data, that needs to be uploaded to **test.guide**. However, there are some prerequisites to use this feature:

- You need to use the json format for the upload of the report data. (see <u style="color: blue;">supported formats</u> for more information)
- A depository needs to be configured in the artifact management.
  - This depository needs to have a storage of type SMB, SFTP, Artifactory or AWS S3 configured.
  - Note, that this storage does not necessarily have to be the active storage of that depository.
- This depository must be the active <u style="color: blue;">file repository</u>.

If these requirements are satisfied, you can upload additional files independently to the report itself:

- First, upload the files to the specified storage that is configured in the depository.
- Second, specify these files in your json report.
  - In the specification of a test case, next to attached artifacts that are included in the Zip file that is being uploaded, specify artifact references to the files like the following.
  - Note, that you have to provide the md5-Hash value of the files content.

<!-- -->

    ...
      {
        "@type": "testcase",
        ...
        "artifacts": [
          "file/in/zip.trace"
        ],
        "artifactRefs": [
          {
            "ref": "\\\\SMB-Host\\Share\\folder\\in\\share\\uploadedFile.trace",
            "md5": "bd01856bfd2065d0d1ee20c03bd3a9af"
          },
          ...
        ]
      }
    ...

- Third, pack this json file together with all files not already uploaded in a zip file and upload it like a normal report upload in the json format.

For more information about the JSON schema download the schema file. Go to the [Import page](https://testguide.one-cx.cn/upload), select a ZIP file and choose JSON2ATX plugin from the drop-down menu. A link for downloading the schema file will appear.lightbulb_2

##### 2.1.1.2.2. How can I upload my ecu.test reports to test.guide?

To upload ecu.test reports to **test.guide**, a connection to **test.guide** must be configured.

This can be achieved in the following ways:

- **Preferred way:** Via the ecu.test \*\*\*\*test.guide\*\*\*\*
  - ![aed167ec2bca396ed8b8d778809fe1fe_MD5](test.guide%20user%20documentation-media/497402ccfe937b4ba097f56823adfa780a9578da.png)
    et Settings
  - a new **test.guide** instance must be created (using the +)
  - the **test.guide** server and port must be configured
  - the following *ATX generator settings* must be set:
    - on the one hand the *uploadAuthenticationKey* (preferably via the created technical user):
      - ![46d31b4591c53fddea880ce02de013ab_MD5](test.guide%20user%20documentation-media/ba9709ed28da50e259413e101ca695640d47ccd8.png)
        AuthKeyFromTechUser
    - on the other hand the *projectId*:
      - this can be determined for the selected project in **test.guide** by looking at the project
      - ![3d35b4250826ac0a6bfd8020b928d111_MD5](test.guide%20user%20documentation-media/643383cb7d2de7cedb2233b533d4d6f54f4da44b.png)
        ProjectIdFromUserProfile
- The same options can also be set via the *TCF ATX report settings*.
  - ![aabb29e41bfd284dc6ac59249a63502a_MD5](test.guide%20user%20documentation-media/829002f7fb1e1295b4437ec392096504db6abf8d.png)
    et TCF Settings
- After configuration (via \*\*\*\*test.guide\*\*\*\*) an upload in the *Test report tab* of ecu.test to the specific instance is possible.
  - ![9e177f35aae5a9ad7aae760970a22bae_MD5](test.guide%20user%20documentation-media/a4ff0a04c5386055140df07276c3f65b4c2e8e7f.png)
    et Upload2TG
  - if configured by the TCF, it must be loaded and activated for execution

##### 2.1.1.2.3. External server upload settings

By default, the required parameters for an upload to test.guide (marked orange) are part of the settings in ecu.test.

- ![7f488219ad1340231eda551625a4d295_MD5](test.guide%20user%20documentation-media/0ff1393d8cd520e7a0999fac2bfa757e971924e4.png)
  et tg settings

To allow for a more flexible configuration *only those parameters can be overridden* with an external JSON file. The configuration parameter *uploadSettings* must point to a file within the ecu.test workspace. The keys correspond to the general settings.

    {
        "url": "192.168.178.134",
        "useHttps": true,
        "port": 8085,
        "contextPath": "/testguide",
        "authKey": "YZiA5tf8ORBCbKq...",
        "proxies": {"https": "...", "http": "..."},
        "projectId": 2
    }

##### 2.1.1.2.4. Why is the name of my test case in test.guide different than in ecu.test?

Reports are transferred to test.guide using the ASAM ATX format in which identifiers must comply with a given schema. For more information see <u style="color: blue;">Limitations imposed by the ATX format</u>. Any identifiers that do not fit the schema are adjusted to allow upload to test.guide. The following changes are made during report generation:

- German umlauts are converted into two vocals, example: "Stoßdämpfer" → "Stossdaempfer"
- special characters are replaced with underscores, as long as they are not the last character of the name, then they are omitted, example: "Test-5(System)" → "Test_5_System"
- white spaces are removed, example: "My test" → "Mytest"
- identifiers starting with numbers will be preceded by an "i", example: "5A" → "i5A"
- leading underscores are omitted, example: "\_test\_" → "test\_"
- finally, multiple underscores in sequence will be reduced to only one underscore, example: "My\_\_test: (speed == 5)" → "My_test_speed_5"

These changes are not only applied to test case names but also to test plan names, constant keys and some other identifiers.

Beginning with version 1.212.0 of the ATX generator a new configuration parameter "extendedCharacterSupport" is available. It allows use of Unicode characters in naming all used components, from the package to the attribute. The name does not have to follow any specific scheme, as long as only permitted characters are used:

- digits zero through nine
- underscore
- hyphen
- any Unicode letter: a--z, A--Z, accented letters like é, ü, ñ, Chinese/Japanese/Arabic characters, etc.

No automatic substitution is applied and instead the generation fails when unsupported characters are used.

error

#### 2.1.1.3. How do I find my test reports of interest?

The [report filter page](https://testguide.one-cx.cn/reports) is a cornerstone of **test.guide**.

<figure>
<img
src="test.guide%20user%20documentation-media/b256d5d0b4f12efb4773a39483158d81eb6a6864.png"
alt="1517ea8f735d0594ce73b483075ab91b_MD5" />
<figcaption
aria-hidden="true">1517ea8f735d0594ce73b483075ab91b_MD5</figcaption>
</figure>

reportfilter

The report filter can be used to create complex filter queries. Just enter your query terms in the filter mask.

Be aware that the filter form is divided into sections, not all filter fields are visible by default.info

The filter and its fields are configurable. See <u style="color: blue;">**Filter settings**</u> lightbulb_2

#### 2.1.1.4. How do I save my complex filters?

Filters can be stored easily in order to use them again at a later date. To do so, click the **Save filter** button.

If you want to allow your colleagues to also use the saved filter, change the filter type setting to **Public filter**.lightbulb_2

If you have the permission for managing projects, also another filter type called **Project filter** will be available. Filters of this type are usable by all project users and in addition, may be used for creating project subscriptions.lightbulb_2

To make the filter easier to use, the **start date** and **end date** can be set relative to the current time. The following keywords can be used:

- "now": current point in time (replaces date and time)
- "today": current date (replaces date and must be followed by a set time)

In addition, Time shifts are possible, for example: "today 19:00 - 1d" (for yesterday 19:00). Available time shifts are plus and minus Minute (min), Hour (h), Day (d), Week (w), Month (m) and Year (y).

#### 2.1.1.5. How can I get notified about new test cases matching my filter?

You can create subscriptions for your actual filter. Use the **Subscribe filter** button above the filter form.

You can also subscribe and unsubscribe to existing project filters. Subscribing to a project filter creates a project subscription, which will be visible to the project manager at <u style="color: blue;">**Project filters**</u>. There the project manager can also delete project subscriptions of the project users or manually create a new project subscription for a project member at any time.lightbulb_2

To use this feature, the email configuration of **test.guide** must be configured correctly. This must be done by an admin and is described at <u style="color: blue;">**Email**</u>.lightbulb_2

#### 2.1.1.6. How do I share a filter quickly?

You can create a link for sharing the filter by using the **Share** above the filter form. The drop-down menu located there also offers additional options for sharing a filter.

#### 2.1.1.7. How do I get detail information for a single test case?

You can analyze a specific test case by clicking on the test case name in the report filter result. This triggers a redirection to the test case detail page. There you can see all executions of the chosen test case. For a specific run, you can use the double arrow button at the end of the line to show further information.

If you want to see a particular test case execution, don't click on the test case name. Instead, directly click on the verdict slot of the run you are interested in.lightbulb_2

#### 2.1.1.8. How do I compare test cases to see what is changed?

In the test case detail view, using the checkboxes, you can select multiple lines. At the bottom of the table is a **Compare selection** button, click it to open the *Test report diff* page for the selected test case executions.

#### 2.1.1.9. How do I analyze tests with parameter variations?

In the test case detail view, using the checkboxes, you can select multiple lines. At the bottom of the table is a **Heatmap** button. Configure the heatmap by selecting the points of interest. Further details are explained on the page directly.

#### 2.1.1.10. How do I restructure the result list of the report filter?

The report filter provides a number of different views for displaying the results. You can select them using the **Active view** drop-down menu above the filter result. At the moment, **test.guide** provides the following views:

<figure>
<img
src="test.guide%20user%20documentation-media/abb81d16d235d0905a9cbbd3c8c4836f270cd990.png"
alt="d92da800e0692dc90c2c1127bc8cfacc_MD5" />
<figcaption
aria-hidden="true">d92da800e0692dc90c2c1127bc8cfacc_MD5</figcaption>
</figure>

reportfilterviews

#### 2.1.1.11. How do I export results to ...

For exporting data, you have to change the active view of the report filter to *Export view*. In this view, select the test case executions to export. By clicking the checkbox in front of a particular line all executions of this test case are selected, while clicking on a verdict slot selects one particular test case execution. Furthermore, there are some selection strategies. You can use them via the **Select all** button and the drop-down menu located next to it.

##### 2.1.1.11.1. ... another test.guide?

To export to another **test.guide** instance, click on the **Test management tool** button and select the target instance. After that, just submit the form.

The other **test.guide** instance has to be configured at <u style="color: blue;">**Management tools**</u>.lightbulb_2

##### 2.1.1.11.2. ... test management tools?

To export to a test management tool, click on the **Test management tool** button and select the tool in the drop-down choice. After that, just submit the form.

The test management tool has to be configured at <u style="color: blue;">**Management tools**</u>. Supported tools are listed at <u style="color: blue;">**Integrating test management tools**</u>.

lightbulb_2

##### 2.1.1.11.3. ... PDF documents?

You can export PDF documents by clicking the button **PDF report**. **test.guide** contains a default test summary report template, which is ready to be used.

If the layout or content of the resulting PDF document does not meet your requirements, you can add custom templates. See <u style="color: blue;">**Customizing the PDF export**</u>.lightbulb_2

##### 2.1.1.11.4. ... Excel documents?

**test.guide** can also export Excel files for your test report data. You can generate it by using the button **Excel**.

##### 2.1.1.11.5. ... or add the selection to a release?

On the right side of report filter result toolbar, there is a **Record release** button and also a drop-down menu offering further options. Using them, you can add the selection to an existing release or create a new release.

#### 2.1.1.12. How do I get test plan focused test report information?

You can use a special page for this feature at ['Testreport management \> Test plans'](https://testguide.one-cx.cn/projects).

### 2.1.2. Using the review feature

With automated test executions, it is common case, that someone has to check the result, especially for failed runs or when errors have occurred. After analyzing the result, you want to save your notes, set a reevaluation or create a ticket. These procedures and many more can be addressed with the review feature.

#### 2.1.2.1. How do I make a review?

You can just click on the reevaluation icon (for the test case execution you want to review) on the test case detail page. The icon may look different depending on the review state: If the execution does not have a review, the icon shows binoculars. If at least one review exists, it shows a clipboard, which is either empty (if the review has no reevaluation) or contains a letter, which represents the reevaluation.

#### 2.1.2.2. How do I create a defect/issue during the review?

You can select an issue tracker in the *Create Ticket in Issue Tracker* drop-down choice. After that, select an issue type and provide all information for the issue form.

It is best practice to first complete the review form and then use the *Create Ticket* feature: In case an issue tracker template exists, the ticket fields can be prefilled with information form the review.lightbulb_2

The issue tracker and (if applicable) the issue tracker template has to be configured before. See <u style="color: blue;">**Issue Tracker**</u>.lightbulb_2

#### 2.1.2.3. How do I reuse my previous reviews?

If you notice, for example, that yesterday's analysis is still applicable, you can also reuse your review of yesterday.

<figure>
<img
src="test.guide%20user%20documentation-media/27ee742012ed99fffb367173dea5191c451807ca.png"
alt="ec07e865f08d0e6aac4fb833cdffe811_MD5" />
<figcaption
aria-hidden="true">ec07e865f08d0e6aac4fb833cdffe811_MD5</figcaption>
</figure>

previousreview

#### 2.1.2.4. How do I bulk review test cases with the same error?

If your analysis shows that there is an error affecting multiple executions of one particular test case, you can do a multi-selection of these items on the *Test report diff* page and click on **Add reviews**. This creates a review for all selected test case executions.

If your analysis shows that there is an error affecting multiple test cases, you can use the *Bulk review* view of the report filter. Filter for the affected test case executions you want to review. Next, multi-select the test cases or particular test case executions and click on **Edit selected test case reports**. On the new page opening, you can further limit your selection and do the bulk review. As a shortcut, if you want to review the whole selection of the report filter page, you can also click **Perform review directly**.

#### 2.1.2.5. How do I perform reviews within ecu.test?

You can also create reviews using **ecu.test**. Reviews created this way are included in the test report that is uploaded from **ecu.test** to **test.guide**. There exist two ways for creating reviews in **ecu.test**:

1.  While the test is executed by using the test step *Report*, which can be found in the category *Default test steps* → *Miscellaneous*. Activate the *Report comment* in order to create a review whose comment is the specified text.
2.  After the test has run by using the TRF-Viewer. Right-click on a test step and select *Manage report comments and revaluations*.

After the review has been created (either way), upload the report to from **ecu.test** to **test.guide** as described in <u style="color: blue;">**Integrating ecu.test**</u>.

Advanced usage

You may have noticed that neither the report test step nor the TRF-Viewer offer to specify the same amount of properties for the review as **test.guide** does.In order to compensate, there is a special syntax for the review comment that allows you to specify more review properties.

| Review property | Syntax example | Notes |
|----|----|----|
| Summary | `#!summary Bus communication failed!#` |  |
| Verdict | `#!verdict FAILED!#` | Using this syntax, the verdict can only be worsened and never improved. Also be aware that the TRF-Viewer will not show the revaluation verdict. |
| Tags | `#!tag buscomm!# or #buscomm#` | The expected tags must be configured in **ecu.test** 's **test.guide** setting *detectReviewTags*. They must match the tags that are configured in the **test.guide** project (see **Review settings**). |
| Defect class | `#!defectClass Moderate!# or \|Moderate\|` | The expected defect classes must be configured in **ecu.test** 's **test.guide** setting *detectReviewDefects*. They must match the defect classes that are configured in the **test.guide** project (see **Review settings**). |

### 2.1.3. Cross-company collaboration

In order to be able to collaborate across project, instance or company boundaries, test.guide offers the possibility to export report data directly to other instances. To do this, test.guide itself must be configured as a test management tool. The data can then be transferred to other projects or instances via the export view.

<figure>
<img
src="test.guide%20user%20documentation-media/9c0e12236930758f339413e4969cde5cc0a294c7.png"
alt="b069fa3dd6b83a8e835046df3d642598_MD5" />
<figcaption
aria-hidden="true">b069fa3dd6b83a8e835046df3d642598_MD5</figcaption>
</figure>

CrossCompanyCollaboration

If direct access to the other test.guide instance is not possible, an ATX document can also be created as a zip file in the export view via the option *Export ATX documents*, which contains all important test report data for the colleagues to import manually. Therefore, a classic exchange via e-mail or exchange drive is also possible at any time.

## 2.2. Using the release management

### 2.2.1. Using the coverage

In projects that follow the V-model, test cases are supposed to verify certain elements from the left side of the V. In the context of requirements based testing, most often these elements are requirements. But one can also think of other specification elements like components of a system's architecture or variants of the system under test that need to be verified. Usually there is a traceability link that connects a test case with the element that it verifies.

The *Coverage filter* in **test.guide** allows you to get insights into the completeness of the testing efforts in your project. A so-called *Coverage Filter Definition* contains all elements from the left side of the V that are relevant to you and connects each of them with a test case filter. This filter selects specifically the test case executions that verify the particular specification element, employing traceability links. **test.guide** can then apply the Coverage Filter Definition to the set of test case executions that were uploaded to produce a *Coverage Filter Result*. This artifact provides information about the completeness of the coverage of your specification elements.

Coverages can be created and managed fully through the GUI or the REST API.lightbulb_2

<figure>
<img
src="test.guide%20user%20documentation-media/b9ac06c010b9f46a5b303ac5d985bb24b2348f71.png"
alt="8176e2bceb21519d8313302ac6d6452e_MD5" />
<figcaption
aria-hidden="true">8176e2bceb21519d8313302ac6d6452e_MD5</figcaption>
</figure>

CoverageScopeRequirementsTree

#### 2.2.1.1. How do I make a coverage?

Coverage is created with the usage of a so-called *coverage filter definition*.

This specifies the criteria to be checked in XML format (see also the corresponding XSD). Examples and further information can be found in the TraceTronic-Example filter definitions for *Cartesian Product* and *Filter Tree General*

``` xml
...
<node>
        <label>Requirements</label>
        <!-- Nodes of the third hierarchy level: -->
        <node>
                <label>Traffic light detection</label>
                <url>http://myreq.company.com/req/42</url>
                <!-- Here, the label of the node (i.e. "Traffic light detection") is
                        used as the scopes value: -->
                <scope name="Crossing assistant" />
                <filters>
                        <attribute name="ReqId">
                                <value>42</value>
                        </attribute>
                </filters>
...
```

The predicates that can be specified are always transformed to individual result filters, so it is important that the criteria to be checked can also be found in the uploaded report as information, e.g. in the form of a constant or an attribute such as the requirements id.

#### 2.2.1.2. How do I use placeholders?

If it only distinguishes the coverage, for example, in regression tests, in the form of a build number or another identifier, a placeholder can be defined in the coverage, which must be specified before execution.

If placeholders are defined without default values, certain features such a coverage subscribing will not work!info

#### 2.2.1.3. How do I create coverages based on my requirements?

If a list or an extract of the requirements to be tested is available, e.g. in Excel, then a script can be used to easily read the *requirements from Excel and convert them into a test.guide coverage filter definition*.

See also chapter: <u style="color: blue;">**X2Coverage (Just "cover" everything...)**</u>

#### 2.2.1.4. How do I create coverages based on test suites of ALM tools?

It is also possible to import test suites directly from ALM as coverage via the ALM import button in the filter definition section.

Therefore, an ALM connection needs to be configured over the <u style="color: blue;">**Management tools**</u>.

This has the advantage, for example, that for very large test suites that take several days to complete, you can use the coverage to check whether all the results are available, i.e. whether all the tests in the planned test suite have been executed.

#### 2.2.1.5. How do I export coverage data?

Coverage data can be queried and processed via the REST API.

However over the *Export to* button in the Coverage filter it is also possible to export the data to Excel or to create a PDF for a coverage report.

### 2.2.2. Using the release train

In **test.guide**, a *Release* is a set of test case executions. *Releases* can be used to collect test case executions that are relevant for an upcoming release of the system under test.

<figure>
<img
src="test.guide%20user%20documentation-media/540cff2c1964737f524aa9ffe4f674b4fee101a3.png"
alt="7b095563ab58f274d923a9f597b62794_MD5" />
<figcaption
aria-hidden="true">7b095563ab58f274d923a9f597b62794_MD5</figcaption>
</figure>

ReleaseTree

You can either manually add test case executions to a *Release* or use a coverage filter to specify which test case executions belong to a *Release*. These are then automatically added as soon as they are uploaded.

Releases can be created and managed fully through the GUI or the REST API.lightbulb_2

<figure>
<img
src="test.guide%20user%20documentation-media/c7320c69a003a7ea191bddafaabcca758e191369.png"
alt="1b5bf910015c42326dca8f49043308bd_MD5" />
<figcaption
aria-hidden="true">1b5bf910015c42326dca8f49043308bd_MD5</figcaption>
</figure>

ReleaseTrainTimeline

#### 2.2.2.1. How do I create a release?

Releases are mapped as tree structures. A release can contain multiple sub-releases.

Release folders (the nodes of the tree) can be created to structure releases, whereas the actual release information comes from the releases (the leaves).

Releases and Release folders can be created over the Release overview. To fill a release with existing test data you can open a report filter in the test report management and either add the results to an existing release or record a new release.

<figure>
<img
src="test.guide%20user%20documentation-media/fa0781e6f63ffa98a66d9f7ee73d52d744aa4e58.png"
alt="2e985f017a840b2dd1930cbc03e8cda3_MD5" />
<figcaption
aria-hidden="true">2e985f017a840b2dd1930cbc03e8cda3_MD5</figcaption>
</figure>

ReleaseAddTestCaseExecution

When creating a release, various metadata such as ticket numbers and release attributes can be specified. This helps in searches, but also offers additional possibilities.

For example, if a release is directly linked to a Jira ticket, all created defect Jira tickets are automatically linked to the release ticket during a review. This makes it easy to track in Jira which bug tickets were created for the release ticket.

If attributes are specified, it is possible that these attributes are automatically mapped to coverage placeholders. So if a placeholder is defined in a coverage, e.g. for a *buildNumber*, and the value is set via the release attribute *buildNumber*, the release attribute is automatically set for the coverage.

To benefit from the full functionality of releases, you should assign a coverage to each release. This means that the progress of a release is automatically determined with each test report upload and an overview is easily possible even at the root release level.lightbulb_2

#### 2.2.2.2. How do I assign a coverage to a release?

When a release (leaf) is created, coverage can be assigned. This is also possible at a later date and the progress of the release is then calculated based on the stored release data.

If a release with coverage is created, this release coverage is duplicated in a separate release folder under the coverage filter definitions.info

#### 2.2.2.3. How do I use the release result?

For each release, the result distribution and, if coverage is specified, the progress is also displayed. If the progress is 100%, this means that all reports to be tested have been uploaded. Now you can see from the result distribution how many faults still need to be fixed or whether the release can be released in this state.

A review with a re-evaluation has a direct effect on the release result distribution for releases that have not been locked!info

#### 2.2.2.4. How do I lock/unlock a release?

When a release is completed, it should also be locked. Because if a release is locked, further changes to the release, e.g. through reviews, are no longer possible. Only a user with the necessary permissions can unlock the release again if a change is still necessary.

Another advantage of locked releases is that they are not taken into consideration when uploading new test reports, so all *uploads are automatically faster*! So if you keep too many releases open with large coverages for a long time, you have to accept that the upload times increase because each upload needs to be checked if it is assigned to a non-locked release.error

#### 2.2.2.5. How do I export release data?

Release data can be queried and processed via the REST API.

However, it is also possible to create *PDF for a test summary report*, by clicking on the drop-down under the Actions button and selecting *Export pdf report*.

If the layout or content of the resulting PDF document does not meet your requirements, you can add custom templates. See <u style="color: blue;">**Reporting**</u>.lightbulb_2

### 2.2.3. Using Quality-Gates (Q-gates)

### 2.2.3. 使用质量门（Q-gates）

Quality gates (Q-gates) enable test processes to be automated beyond simple continuous testing.

Quality gates (Q-gates) 能够使 test 流程的自动化超越简单的持续测试（continuous testing）。

They prevent, for example, test artifacts from being processed further if the test criteria for the artifact are not met. But at the same time, it is also possible to pass the artifacts on to other teams, to inform colleagues via mail or to start further tests for successful tests.

例如，如果 test artifact 未满足其 test criteria，Q-gates 会阻止这个 artifact 进一步被处理。但同时，也可以将 artifacts 传递给其他团队、通过邮件通知同事，或为成功的 tests 启动进一步的 tests。

With the help of Q-gates, it is **possible to achieve easier control of the processes in the project through staging**.

借助 Q-gates 的帮助，**通过 staging（*分阶段管理* 或 *分级控制*），可以实现对项目中的流程进行更简便的控制**。

Q-gates can be created and managed fully through the GUI or the REST API.lightbulb_2

Q-gates 可以完全通过 GUI 或 REST API 来创建和管理。

<figure>
<img
src="test.guide%20user%20documentation-media/7376d3482293f38301d947837f062532c91afbff.png"
alt="31e2f3aa70bb9d92c06e4348c1e77f3f_MD5" />
<figcaption
aria-hidden="true">31e2f3aa70bb9d92c06e4348c1e77f3f_MD5</figcaption>
</figure>

PreConditionQualityGateGraph

#### 2.2.3.1. How do I set up a Q-gate staging?

#### 2.2.3.1. 我如何设置 Q-gate staging？

Staging involves creating a Q-gate plan that describes the process for releasing a test artifact, for example.

Staging 涉及创建一个 Q-gate plan，该计划描述发布 test artifact 的流程，例如。

If the plan has been developed, it can be started. This is similar to an automation pipeline that is designed and activated. However, the difference with Q-gate plans is that each plan is created for a specific process execution. If you want to use a Q-gate plan to validate different versions of a test artifact, you have to create a new Q-gate plan for each version of the test artifact. The simplest approach is then to copy the old plan when the commit is triggered and, if necessary, only change the parameters for the new test artifact to be tested and start the plan for the release.

计划开发完成后，可以启动它。这类似于设计和激活的 automation pipeline。但 Q-gate plans 的区别在于，每个 plan 都是为特定的 process execution 创建的。如果你想用一个 Q-gate plan 来验证 test artifact 的不同版本，必须为每个版本创建一个新的 Q-gate plan。最简单的方法是当 commit 被触发时复制旧计划，如有必要，仅更改要测试的新 test artifact 的参数，然后启动 release plan。

Q-gate states only change after the plan has been started. After starting the plan execution changing, adding or deleting plan elements is no longer possible, but it is possible to add attributes to the plan or to update these. When creating a new plan, the following states exist:

Q-gate 的状态仅在计划启动后才会改变。启动 plan execution 后，不再可能改变、添加或删除 plan elements，但可以向 plan 添加 attributes 或更新这些 attributes。创建新 plan 时，存在以下状态：

- *UNDER_CONSTRUCTION* - if the plan is currently being created and has not yet started.

- *UNDER_CONSTRUCTION*（*构建中*）- 如果 plan 当前正在创建且尚未启动。

- *IN_EXECUTION* - if the plan has been started.

- *IN_EXECUTION*（*执行中*）- 如果 plan 已启动。

- *INVALIDATED* - if the plan has been cancelled, for example, because of a misconfiguration.

- *INVALIDATED*（*已失效*）- 如果 plan 已被取消，例如由于配置错误。

- *FINALIZED* - if the plan has been completed

- *FINALIZED*（*已完成*）- 如果 plan 已完成。

A new plan can be created over the plan overview with add plan.

可以通过 plan overview 的 add plan 功能创建新 plan。

#### 2.2.3.2. Which Q-gates are there?

#### 2.2.3.2. 有哪些 Q-gates？

There are currently six different Q-gates:

目前有六种不同的 Q-gates：

- A *Manual Q-gate*, which is equivalent to a switch. Here the user can trigger an action either via the GUI or REST-API. This can be used, for example, to confirm a release or for automation by an external system.

- *Manual Q-gate*（*手动门*），相当于一个 switch。用户可以通过 GUI 或 REST-API 触发一个 action。这可以用来确认 release，或由外部系统进行自动化。

- A *Approval Q-gate*, is similar to a *Manual Q-gate*. The gate can be used to ensure that users explicitly approve further processing. No *STOPPED* states are automatically propagated until a user has explicitly approved them.

- *Approval Q-gate*（*审批门*），类似于 *Manual Q-gate*。该 gate 用于确保用户显式地批准进一步的处理。*STOPPED* 状态在用户显式批准之前不会自动传播。

- A *Release Q-gate* is based on a defined test.guide release (with coverage) and is switched automatically as soon as the defined release conditions are fulfilled.

- *Release Q-gate*（*发布门*）基于已定义的 test.guide release（带有 coverage），一旦满足定义的 release conditions，就会自动切换。

- The *Join Q-gate* is a connecting Q-gate that waits for several Q-gate results and combines the current status. This is useful for better visualizing important milestones in the validation process.

- *Join Q-gate*（*连接门*）是一个连接 Q-gate，它等待多个 Q-gate 的结果并组合当前状态。这对于更好地可视化 validation process 中的重要里程碑很有用。

- A *Pull Q-gate* uses the state of a shared Q-gate from another Q-gate plan, project or test.guide instance. See chapter <u style="color: blue;">Sharing and pulling Q-gate states</u> for details.

- *Pull Q-gate*（*拉取门*）使用来自另一个 Q-gate plan、project 或 test.guide instance 的 shared Q-gate 的状态。详见章节 <u style="color: blue;">Sharing and pulling Q-gate states</u>。

- A *Workflow Q-gate* is designed to integrate with the <u style="color: blue;">Workflow Automation</u>. Once its preconditions are met, it will trigger a new flow task execution via the specified flow trigger. The Q-gate will switch to either the *STOPPED* or *PASSED* state after the flow task is finished, depending on its final state. This will allow staging to continue or halt the staging process.

- *Workflow Q-gate*（*工作流门*）用于与 <u style="color: blue;">Workflow Automation</u> 集成。一旦满足其 preconditions，它将通过指定的 flow trigger 触发新的 flow task execution。flow task 完成后，Q-gate 根据其最终状态切换为 *STOPPED* 或 *PASSED* 状态。这样可以使 staging 继续进行或停止 staging process。

#### 2.2.3.3. How do Q-gates interact with each other?

#### 2.2.3.3. Q-gates 如何相互作用？

Q-gates switch depending on their state.

Q-gates 根据其状态进行切换。

Q-gates can have 4 different states (in order of increasing state weight):

Q-gates 有 4 种不同的状态（按状态权重递增的顺序）：

- *UNDEFINED*, if there is no result for this stage available

- *UNDEFINED*（*未定义*），如果此阶段没有可用的结果。

- *IN_PROGRESS*, if all preconditions for the stage are fulfilled but the Q-gate itself does not yet have a result.

  - 💡 This means that all Q-gates are automatically in progress if they have no preconditions!

- *IN_PROGRESS*（*进行中*），如果该阶段的所有 preconditions 都满足，但 Q-gate 本身还没有得到结果。

  - 💡 这意味着如果 Q-gates 没有 preconditions，则它们会自动处于进行中状态！

- *PASSED*, if the stage is fulfilled

- *PASSED*（*通过*），如果该阶段被满足。

- *STOPPED* if the stage is not fulfilled

- *STOPPED*（*停止*），如果该阶段未被满足。

Q-gates can be connected to each other, which means that a Q-gate can define as an input condition that one or more other Q-gate results must be finished. This is how the different Q-gate states are achieved.

Q-gates 可以相互连接，这意味着一个 Q-gate 可以定义 input condition，即一个或多个其他 Q-gate 的结果必须完成。这是如何实现不同 Q-gate 状态的。

On the one hand, it is important to know that STOPPED has a high priority and is propagated immediately through a Q-gate plan, so that the analysis can start immediately in the event of problems.

一方面，重要的是要知道 STOPPED 具有高优先级，会立即在 Q-gate plan 中传播，以便在出现问题时立即开始分析。

On the other hand, if a Q-gate is PASSED, it always remains PASSED and cannot be changed. 💡 A release Q-gate with STOPPED can still be switched to PASSED, for example, by a PASSED re-evaluation.

另一方面，如果 Q-gate 是 PASSED，它将始终保持 PASSED 状态，不能更改。💡 一个状态为 STOPPED 的 release Q-gate 仍然可以通过例如 PASSED 的重新评估（*re-evaluation*）切换为 PASSED。

error

#### 2.2.3.4. Sharing and pulling Q-gate states

#### 2.2.3.4. 共享和拉取 Q-gate 状态

Q-gates can be *shared* across Q-gate plans, projects or even test.guide instances. The state of these shared Q-gates is then accessible via so called *Pull Q-gates*. Technically, this is achieved via a REST API. For authorization, every shared Q-gate specifies which project roles are allowed to access it. For authentication, a technical user is usually used who must have at least one of the specified project roles.

Q-gates 可以在 Q-gate plans、projects 甚至 test.guide instances 之间 *共享*。这些 shared Q-gates 的状态随后可通过所谓的 *Pull Q-gates* 访问。从技术上讲，这是通过 REST API 实现的。对于授权，每个 shared Q-gate 都指定允许访问它的 project roles。对于认证（*authentication*），通常使用 technical user，该用户必须至少具有一个指定的 project roles。

The following procedure is usually advisable to use this feature. At the sharing party:

使用此功能通常建议遵循以下步骤。在 sharing party 端：

- Create a specific project role for the share.

- 为共享创建特定的 project role。

- Create a technical user and assign this project role.

- 创建 technical user 并分配此 project role。

- Create an authentication key for the technical user.

- 为 technical user 创建 authentication key。

- Assign the project role to the Q-gate to be shared.

- 将 project role 分配给要共享的 Q-gate。

At <u style="color: blue;">**Settings**</u>, by clicking the *Create user and project role to share Q-gates* button and using the opened dialog, these steps can be carried out in one operation.info

在 <u style="color: blue;">**Settings**</u> 处，点击 *Create user and project role to share Q-gates* 按钮并使用打开的对话框，可以在一个操作中执行这些步骤。

The other party attempting to retrieve the status of the shared Q-Gate must be provided with the connection data of the sharing test.guide instance (URL and project ID) and the authentication key of the technical user:

试图检索 shared Q-Gate 状态的另一方必须获得 sharing test.guide instance 的连接数据（URL 和 project ID）以及 technical user 的 authentication key：

- Create a new tool of the type *test.guide* with this data at <u style="color: blue;">**Management tools**</u>.

- 在 <u style="color: blue;">**Management tools**</u> 处使用此数据创建 *test.guide* 类型的新 tool。

- Create a Pull Q-gate in the desired Q-gate plan. A filter is defined which must unambiguously determine the shared Q-gate, and additionally the authentication key is specified with which the Pull Q-gate identifies itself at the sharing party.

- 在所需的 Q-gate plan 中创建 Pull Q-gate。定义一个 filter，它必须明确地确定 shared Q-gate，并且另外指定 authentication key，Pull Q-gate 用此 key 在 sharing party 端进行身份识别（*identifies itself*）。

## 2.3. Using the monitoring of test resources

## 2.3. 使用 test resources 的监控

A new module called *Test infrastructure* is currently under development. Some features of the monitoring module will be successively integrated into this new module.info

一个名为 *Test infrastructure* 的新 module 目前正在开发中。监控 module 的某些功能将逐步集成到这个新 module 中。

Using the test infrastructure management

使用 test infrastructure 管理

All content within this collapsible section describe features of the development preview of the new module *Test infrastructure*. Please be aware that changes are possible at any time. Any kind of feedback is well appreciated. Please contact us at [support@tracetronic.com](mailto:support@tracetronic.com?subject=test.guide%20Test%20infrastructure%20module%20feedback&body=Your%20feedback%20goes%20here%26%238230%3B%26%238203%3B).error

此可折叠部分内的所有内容描述新 module *Test infrastructure* 的开发预览版功能。请注意随时可能会发生更改。非常感谢任何反馈。请通过 [support@tracetronic.com](mailto:support@tracetronic.com?subject=test.guide%20Test%20infrastructure%20module%20feedback&body=Your%20feedback%20goes%20here%26%238230%3B%26%238203%3B) 与我们联系。

You can manage your <u style="color: blue;">**test infrastructure**</u> in **test.guide**. Therefore, you can create <u style="color: blue;">**test resource**</u> s and <u style="color: blue;">**test resource machine**</u> s, add information such as attributes and/or connect a sensor/client called *<u style="color: blue;">**ResourceAdapter**</u>*. Beneath filtering and the live view of test resource machines with a **ResourceAdapter** connected, you can distribute test executions to your test resource machines (see <u style="color: blue;">Using the test execution</u>).

你可以在 **test.guide** 中管理你的 <u style="color: blue;">**test infrastructure**</u>。因此，你可以创建 <u style="color: blue;">**test resource**</u> 和 <u style="color: blue;">**test resource machine**</u>，添加属性等信息和/或连接一个称为 *<u style="color: blue;">**ResourceAdapter**</u>* 的 sensor/client。除了对连接 **ResourceAdapter** 的 test resource machines 的过滤和实时视图外，你可以将 test executions 分配给你的 test resource machines（见 <u style="color: blue;">Using the test execution</u>）。

**Test resources and test resource machines**
**Test resources 和 test resource machines**

**test.guide** defines two levels for managing test infrastructure: *test resource (TR)* and *test resource machine (TRM)*. A TRM is always a child of exactly one TR. The other way round, a TR can consist of multiple TRMs. The main reason for this two-level hierarchy is the need to map complex (mainly hardware) test benches that are controlled by more than one PC. Here, the TR level corresponds to the test bench itself and the TRM level to the individual PCs. In most cases, a 1:1 relationship between TR and TRM is recommended.

**test.guide** 定义了两个级别来管理 test infrastructure：*test resource (TR)* 和 *test resource machine (TRM)*。一个 TRM 始终是恰好一个 TR 的 child。反过来说，一个 TR 可以包含多个 TRMs。这种两级层次结构的主要原因是需要映射由多个 PC 控制的复杂（主要是硬件）test benches。在这里，TR level 对应于 test bench 本身，TRM level 对应于单个 PCs。在大多数情况下，建议 TR 和 TRM 之间为 1:1 的关系。

Existing users may know these two levels from the *ResourceLocationId*, where they were the 4th and 5th element, formerly known as *test bench* and *machine*.info

现有用户可能从 *ResourceLocationId* 中知道这两个级别，它们曾是第 4 和第 5 个元素，以前称为 *test bench* 和 *machine*。

The picture below shows the general structure of TRs, TRMs and their relationship.

下面的图片展示了 TRs、TRMs 及其关系的总体结构。

<figure>
<img
src="test.guide%20user%20documentation-media/1b9a54c5667b4dd38e159d2d28ddee3f32701578.png"
alt="f594b992904a1db99019de65ed9aa17f_MD5" />
<figcaption
aria-hidden="true">f594b992904a1db99019de65ed9aa17f_MD5</figcaption>
</figure>

Each test resource in **test.guide** receives a UUID, called TR-ID and gets both a location and a name. Each test resource machine also receives a UUID, called TRM-ID and gets a name. There are different kind of data that are stored either at the TR or at the TRM level. The following table provides an overview of the different data types.

**test.guide** 中的每个 test resource 都会获得一个称为 TR-ID 的 UUID，并获得位置和名称。每个 test resource machine 也会获得一个称为 TRM-ID 的 UUID，并获得名称。有不同种类的数据存储在 TR 或 TRM level。下表概述了不同的数据类型。

Data \| Level \| Purpose \|\
数据 \| 级别 \| 目的 \|\
--- \| --- \| --- \|\
Attributes \| TR \| Additional information to define a TR that can be added by the user \|\
Attributes（属性） \| TR \| 可由用户添加的用来定义 TR 的附加信息 \|\
Appointments \| TR \| Booking of test resource in a TR-calendar \|\
Appointments（预约） \| TR \| TR-calendar 中 test resource 的预定 \|\
Monitoring Data \| TRM \| Information regarding the TRM mainly gathered by the **ResourceAdapter** \|\
Monitoring Data（监控数据） \| TRM \| 关于主要由 **ResourceAdapter** 收集的 TRM 的信息 \|

**Pages in the test.guide UI for managing the test infrastructure**
**test.guide UI 中用于管理 test infrastructure 的页面**

There are different pages to get all jobs done regarding the management of test infrastructure. Please find an overview below. Functions that can be used from the pages are described in the following text.

有不同的页面可以完成所有与 test infrastructure 管理相关的工作。请查看下面的概览。可从这些页面使用的功能在以下文本中描述。

Page *Test resource overview* (TR overview)

页面 *Test resource overview*（TR overview）

- Main Purpose: Filter and find all test resources within the respective project.

- 主要目的：在各自的 project 中过滤和查找所有 test resources。

- How to get there? In the main navigation bar select \[ **Test resources**\].

- 如何到达？在主导航栏中选择 \[ **Test resources**\]。

Page *Activity distribution*

页面 *Activity distribution*（活动分布）

- Main Purpose: Find out which activities were carried out on the TR and its TRMs as a percentage.

- 主要目的：以百分比形式找出在 TR 及其 TRMs 上执行的活动。

- How to get there? In the main navigation bar select \[ **Activity**\].

- 如何到达？在主导航栏中选择 \[ **Activity**\]。

*Settings page*

*Settings 页面*

- Main Purpose: Change settings regarding test infrastructure e.g. activity types.

- 主要目的：更改有关 test infrastructure 的设置，例如 activity types。

- How to get there? In the main navigation bar select \[ **Settings**\].

- 如何到达？在主导航栏中选择 \[ **Settings**\]。

*Test resource detail page* (TR detail page)

*Test resource 详情页面*（TR detail page）

- Main Purpose: See all information belonging to a specific test resource.

- 主要目的：查看属于特定 test resource 的所有信息。

- How to get there?

- 如何到达？

  - At the *TR overview* click on the name of a test resource.

  - 在 *TR overview* 上点击 test resource 的名称。

  - At the *TRM detail page* click on the TR icon in the upper right toolbar.

  - 在 *TRM detail page* 上点击右上工具栏中的 TR 图标。

  - At the *Comparison of test resource configurations* click on the name of a test resource.

  - 在 *Comparison of test resource configurations*（*test resource 配置比较*）上点击 test resource 的名称。

  - At the *Booking view* click on the name of a test resource.

  - 在 *Booking view*（*预定视图*）上点击 test resource 的名称。

*Test resource machine detail page* (TRM detail page)

*Test resource machine 详情页面*（TRM detail page）

- Main Purpose: See all information belonging to a specific test resource machine.

- 主要目的：查看属于特定 test resource machine 的所有信息。

- How to get there?

- 如何到达？

  - At the *TR overview* click on the TRM icon in the column "TRM".

  - 在 *TR overview* 上点击"TRM"列中的 TRM 图标。

  - At the *TR detail page* click on the TRM name within the TRM panel.

  - 在 *TR detail page* 上，点击 TRM panel 中的 TRM 名称。

- ==This page is deprecated.== The TRM information will be moved to the *TR detail page* in the future!

- ==此页面已弃用（*deprecated*）。== TRM 信息将来会被移到 *TR detail page* 上！

Page *Comparison of test resource configurations*

页面 *Comparison of test resource configurations*（*Test resource 配置比较*）

- Main Purpose: Compare multiple test resources by the configurations items of the underlying TRMs.

- 主要目的：通过底层 TRMs 的配置 items 比较多个 test resources。

- How to get there? At the *TR overview* select at least two TRs and click on **Compare configurations** on the bottom of the page.

- 如何到达？在 *TR overview* 上选择至少两个 TRs，然后点击页面底部的 **Compare configurations**。

Page *Booking view*

页面 *Booking view*（*预定视图*）

- Main Purpose: Find a suitable time slot within multiple TR calendars.

- 主要目的：在多个 TR calendars 中找到合适的时间段。

- How to get there? At the *TR overview* select at least one TR and click on **Booking view** on the bottom of the page.

- 如何到达？在 *TR overview* 上选择至少一个 TR，然后点击页面底部的 **Booking view**。

Page *Central **ResourceAdapter** settings*

页面 *Central **ResourceAdapter** settings*（*中央 **ResourceAdapter** 设置*）

- Main Purpose: Change **ResourceAdapter** configurations e.g. to activate a new plug-in.

- 主要目的：更改 **ResourceAdapter** 配置，例如激活新 plug-in。

- How to get there? In the main navigation bar select \[ **ResourceAdapters**\] (Monitoring management rights are required).

- 如何到达？在主导航栏中选择 \[ **ResourceAdapters**\]（需要 Monitoring management rights）。

Page *Monitoring database settings*

页面 *Monitoring database settings*（*监控数据库设置*）

- Main Purpose: Configure the settings for the monitoring database connection.

- 主要目的：配置 monitoring database connection 的设置。

- How to get there? In the main navigation bar select \[ **Monitoring**\] (Server Admin rights are required).

- 如何到达？在主导航栏中选择 \[ **Monitoring**\]（需要 Server Admin rights）。

Page *Monitoring IT view*

页面 *Monitoring IT view*（*监控 IT 视图*）

- Main Purpose: Overview of all test benches within the respective **test.guide** project (based on the information in the ResourceLocationId).

- 主要目的：各自 **test.guide** project 中所有 test benches 的概览（基于 ResourceLocationId 中的信息）。

- How to get there? In the main navigation bar select \[ **IT View**\].

- 如何到达？在主导航栏中选择 \[ **IT View**\]。

- ==This page is deprecated== and it will be replaced by the *TR overview*.

- ==此页面已弃用==，将被 *TR overview* 替代。

**Create new TRs and TRMs**
**创建新的 TRs 和 TRMs**

New test resources and test resource machines can be created within an existing **test.guide** project via the GUI or the API. To do so, you need the **Monitoring management** rights.

可以通过 GUI 或 API 在现有的 **test.guide** project 中创建新的 test resources 和 test resource machines。为此，你需要 **Monitoring management** rights。

- Creation of a new TR can be done using the button **Create TR** at the *TR overview*.

- 可以使用 *TR overview* 上的 **Create TR** 按钮创建新的 TR。

- To create a new TRM, please go to the *TR detail page* of the desired parent test resource and click on **Create TRM** within the TRM panel.

- 要创建新的 TRM，请转到所需 parent test resource 的 *TR detail page*，然后点击 TRM panel 中的 **Create TRM**。

When creating a new TRM using the API, a parent TR-ID is required. Since creating test resources and test resource machines is possible within **test.guide**, a connected **ResourceAdapter** is no longer a prerequisite for the creation of a TR and TRM (as beforehand). Accordingly, TRs and TRMs can exist without a **ResourceAdapter**.

使用 API 创建新 TRM 时，需要 parent TR-ID。由于在 **test.guide** 中可以创建 test resources 和 test resource machines，连接的 **ResourceAdapter** 不再是创建 TR 和 TRM 的必需条件（与以前不同）。因此，TRs 和 TRMs 可以在没有 **ResourceAdapter** 的情况下存在。

**Connecting a ResourceAdapter to a TRM**
**将 ResourceAdapter 连接到 TRM**

By connecting a **ResourceAdapter** to a TRM, monitoring data from the machine on which the **ResourceAdapter** is running can be collected. A so called "ResourceLocationId" is required for this. The ResourceLocationId will be replaced by the new TR-ID and TRM-ID in the future. To ensure the easiest possible transition for existing connected test benches, TR- and TRM-IDs will be created automatically when new data of a connected **ResourceAdapter** is processed by **test.guide**. The information from the ResourceLocationId is automatically linked and appended to the generated TR and TRMs as follows:

通过将 **ResourceAdapter** 连接到 TRM，可以收集运行 **ResourceAdapter** 的机器上的 monitoring data。为此需要一个所谓的"ResourceLocationId"。ResourceLocationId 将来会被新的 TR-ID 和 TRM-ID 所取代。为了确保现有已连接的 test benches 的最平稳过渡，当连接的 **ResourceAdapter** 的新数据由 **test.guide** 处理时，TR- 和 TRM-IDs 将自动创建。来自 ResourceLocationId 的信息会自动链接并追加到生成的 TR 和 TRMs，如下所示：

<table>

<colgroup>

<col>

<col>

<col>

<col>

<col>

<col>

</colgroup>

<thead>

<tr>

<th>

ResourceLocationId
</th>

<th colspan="5">

Building/Level/Room/TestBench/Machine
</th>

</tr>

</thead>

<tbody>

<tr>

<td>

<p>

Elements
</p>

</td>

<td>

<p>

Building
</p>

</td>

<td>

<p>

Level
</p>

</td>

<td>

<p>

Room
</p>

</td>

<td>

<p>

TestBench
</p>

</td>

<td>

<p>

Machine
</p>

</td>

</tr>

<tr>

<td>

<p>

Test resource
</p>

</td>

<td colspan="3">

<p>

Location
</p>

</td>

<td>

<p>

Name
</p>

</td>

<td>

<p>

\-
</p>

</td>

</tr>

<tr>

<td>

<p>

Test resource machine
</p>

</td>

<td colspan="4">

<p>

\-
</p>

</td>

<td>

<p>

Name
</p>

</td>

</tr>

</tbody>

</table>

As long as the ResourceLocationId exists, starting a **ResourceAdapter** with a new ResourceLocationId (see also <u style="color: blue;">How do I add a new test resource to my **test.guide** project?</u>) will result in automated creation of the corresponding TR and TRM. Later on, TR and TRM must be created in **test.guide** first. At the same time, the *Location* and *Name* information of TRs and TRMs is read-only and the location must consist of the three parts "Building", "Level" and "Room" separated by a slash.

只要 ResourceLocationId 存在，使用新的 ResourceLocationId 启动 **ResourceAdapter**（另参见 <u style="color: blue;">How do I add a new test resource to my **test.guide** project?</u>）将导致相应 TR 和 TRM 的自动创建。以后，TR 和 TRM 必须先在 **test.guide** 中创建。同时，TRs 和 TRMs 的 *Location* 和 *Name* 信息是只读的，位置必须由"Building"、"Level"和"Room"三部分组成，用斜线分隔。

To connect a **ResourceAdapter** after creating TR and TRM in **test.guide** please ensure that the ResourceLocationId contains all necessary information from the TR and TRM. For example to connect a **ResourceAdapter** to a TRM with the name "PC1" that is the child of a TR named "HiL1" with the location "HQ/Level2/Room2.5" the resulting ResourceLocationId will be "HQ/Level2/Room2.5/HiL1/PC1".

在 **test.guide** 中创建 TR 和 TRM 后，如要连接 **ResourceAdapter**，请确保 ResourceLocationId 包含来自 TR 和 TRM 的所有必要信息。例如，要将 **ResourceAdapter** 连接到一个名为"PC1"的 TRM，该 TRM 是名为"HiL1"的 TR 的子项，位置为"HQ/Level2/Room2.5"，则生成的 ResourceLocationId 将为"HQ/Level2/Room2.5/HiL1/PC1"。

Changing the ResourceLocationId of an existing **ResourceAdapter** will cause the creation of a new TR- and TRM-ID!error

更改现有 **ResourceAdapter** 的 ResourceLocationId 将导致创建新的 TR- 和 TRM-ID！

**Remove TRs and TRMs**
**移除 TRs 和 TRMs**

The deletion of test resources and test resource machines is possible via the GUI and API. The *TR overview page* provides the ability to delete multiple TRs at once. The *TR detail page* provides a button to delete the currently displayed TR and buttons to delete underlying TRMs. **Monitoring management** rights are required for this.

可以通过 GUI 和 API 删除 test resources 和 test resource machines。*TR overview page* 提供了一次删除多个 TRs 的能力。*TR detail page* 提供了删除当前显示的 TR 的按钮和删除底层 TRMs 的按钮。这需要 **Monitoring management** rights。

When a TR is deleted via the GUI, all associated custom attribute entries and underlying TRMs with all their data will be deleted as well! Deleting a TR via the API requires all underlying TRMs to be deleted first. When deleting a single TRM, all monitoring data belonging to this TRM will be deleted as well.

通过 GUI 删除 TR 时，所有关联的自定义 attribute entries 和底层 TRMs 以及它们的所有数据也会被删除！通过 API 删除 TR 需要先删除所有底层 TRMs。删除单个 TRM 时，属于此 TRM 的所有 monitoring data 也将被删除。

The deletion process may take a while, depending on the amount of data attached to a TRM. Please deactivate all **ResourceAdapter** s before deleting a TR or TRMs, if any are connected.

删除过程可能需要一段时间，具体取决于附加到 TRM 的数据量。如果连接了任何 **ResourceAdapters**，请在删除 TR 或 TRMs 之前停用它们。

**Add data to TRs and TRMs**
**向 TRs 和 TRMs 添加数据**

**Calendars and appointments**
**日历和预约**

To improve collaboration on a shared test resource a calendar for a TR can be used. By adding appointments the resource can be "booked". These booking features only exist on TR-level, because booking a single PC of a test bench makes no sense (see the two-level hierarchy of TR and TRM described above).

为了改进对 shared test resource 的协作，可以使用 TR 的 calendar。通过添加 appointments，可以"预定"该资源。这些预定功能仅存在于 TR-level，因为对 test bench 的单个 PC 进行预定没有意义（见上文描述的 TR 和 TRM 的两级层次结构）。

When creating a TR, a corresponding calendar is automatically created on the *TR detail page* and can be used to add appointments. An appointment consists of at least a subject, a start- and an end-time. Furthermore, additional content can be provided in the body and a category can be assigned. Categories has to be defined beforehand on the *Settings page* (**Monitoring management** rights are required for this). Each category has a user defined color. The appointments belonging to a category are displayed in the calendar in the respective color.

创建 TR 时，会在 *TR detail page* 上自动创建相应的 calendar，可用于添加 appointments。一个 appointment 至少包含 subject、start-time 和 end-time。此外，可以在 body 中提供额外的内容，并可以分配 category。Category 必须事先在 *Settings page* 上定义（需要 **Monitoring management** rights）。每个 category 都有用户定义的颜色。属于某个 category 的 appointments 会以相应的颜色显示在 calendar 中。

Appointments can be edited and deleted by users with the appropriate rights (**Monitoring data: Create/Update and Delete**). For bette traceability and collaboration the user and the time of creation and the last change are stored as metadata and displayed.

具有适当权限的用户可以编辑和删除 appointments（**Monitoring data: Create/Update and Delete**）。为了更好地进行追溯和协作，创建者、创建时间和最后更改时间都作为元数据存储并显示。

API endpoints for managing TR-appointments are also available.

也可以使用 API endpoints 来管理 TR-appointments。

**Attributes for test resources**
**Test resources 的属性**

For a better description of your test resources, attributes can be defined at **test.guide** project level. **Monitoring management** rights are required to create these attributes on the *Settings page*. The defined attributes can then be filled with values for each TR (so-called *custom attribute entries*). Currently, only strings are supported. The right to create and update monitoring data is required to fill the values. The attributes are visible and their values are editable on the *TR detail page*.

为了更好地描述你的 test resources，可以在 **test.guide** project 级别定义 attributes。在 *Settings page* 上创建这些 attributes 需要 **Monitoring management** rights。然后可以为每个 TR 使用值填充已定义的 attributes（所谓的 *custom attribute entries*）。目前仅支持 strings。填充值需要创建和更新 monitoring data 的权限。attributes 在 *TR detail page* 上可见，其值可编辑。

Managing attributes is also possible using the Test infrastructure API.

也可以使用 Test infrastructure API 来管理 attributes。

To "delete" a single entry manually, please send the value `*null*` using the endpoint `POST api/testinfrastructure/customattributeentries`.info

要手动"删除"单个 entry，请使用 endpoint `POST api/testinfrastructure/customattributeentries` 发送值 `*null*`。

**Monitoring data**
**监控数据**

To keep informed about states, activities and more details regarding a single test resource machine, monitoring data can be collected by a connected **ResourceAdapter**. Please refer to further chapters from <u style="color: blue;">How do I add a new test resource to my **test.guide** project?</u> for setting up and using this feature.

为了及时了解关于单个 test resource machine 的状态、活动和更多细节，可以通过连接的 **ResourceAdapter** 收集 monitoring data。请参考 <u style="color: blue;">How do I add a new test resource to my **test.guide** project?</u> 中的进一步章节，了解如何设置和使用此功能。

**Using test resources and test resource machines**
**使用 test resources 和 test resource machines**

**Test resources overview**
**Test resources 概览**

At the *Test resource overview* page, a list of all TRs and their <u style="color: blue;">aggregated state</u> is displayed. On this page, TRs can be filtered based on different information, e.g. configuration items or attributes. Selection of TRs e.g. for comparisons is also possible here.

在 *Test resource overview* 页面上，显示了所有 TRs 和它们的 <u style="color: blue;">aggregated state</u> 列表。在此页面上，TRs 可以根据不同信息（例如 configuration items 或 attributes）进行过滤。也可以在此处选择 TRs，例如用于比较。

**Filtering of test resources**
**过滤 test resources**

The filtering of test resources is mainly based on the data, that is attached to them or their underlying TRMs. Filtering is only possible by TR name, locations, configuration items and attributes. Those filters are performend in multiple steps:

Filtering by **test resource name**

1.  Filtering of the *Value*

Filtering by **locations** of a TR:

1.  Filtering of the *Value(s)*

Filtering by **configuration items** of underlying TRMs:

1.  Filtering of the *Key*, which consists of *Category* and *Label* of the configuration item
2.  Filtering of the *Value(s)*

Filtering by **attributes** of a TR:

1.  Filtering of the *Key*, which is the *name of the custom attribute*
2.  Filtering of the *Value(s)*, which is the corresponding *custom attribute entry*

To make filtering of complex expressions for configuration items easier, quick filters for the *Category/Label* level can be defined by a user with **Monitoring management** rights by clicking on the disk-button in the filter area after entering a filter expression (see image below). After saving a quick filter it can be used by any project user with the right to see the test resource list. Quick filters are only available for configuration items. Deleting quick filters also requires the Monitoring management rights and can be done by clicking on the `x` at the beginning of the respective quick filter button.

If there are several values available, more than one entry can be selected for the values. The selection of several values corresponds to an `OR` link in filtering. In the following example, all TRs will be shown, which have TRMs with the configuration item `SOFTWARE/Notepad++ Team/Notepad++` with the value `8.1.5` **or** `8.4.2`. This could be the case, when the software scan plug-in of the ResourceAdapter detected an installed Notepad++ with one of the mentioned versions.

If several keys are used for filtering, the individual elements are `AND` -linked on the test resource level. In the example shown below, all TRs will be shown, which have TRMs with the configuration item `SOFTWARE/Notepad++ Team/Notepad++` with the value `8.4.2` **and** with the configuration item `SOFTWARE/tracetronic GmbH, Dresden/ecu.test 2024.1` with the value `*`. This could mean for example that you are looking for a TR with a specific version of Notepad++ **and** any version of an ecu.test 2024.1, e.g. ecu.test 2024.1.2.0.

This applies to both two-step filters (custom attribute and configuration). Generally, each filter criterion must be fulfilled by the TR or at least one of its underlying TRMs. It is not necessary that one or more underlying TRMs fulfill all filter criteria.

Wildcards such as `*` can be used. When using wildcards for both key and value within a filter, only TRs that have values for the respective key or for which the underlying TRMs have values for the respective key are displayed. E.g. filtering attributes by the expression `*:*` will only return TRs having any values (that are not equal to `null`) for any custom attribute.

**Compare test resources by their configurations**

To compare multiple test resources, you can select the desired TRs on the left-hand side and click **Compare configurations**. You can use the same features known from other comparisons in **test.guide**.

The comparison of test resources is based on configuration items of their associated TRMs. If more than one TRM has the same configuration item, only the latest value is displayed.error

**Find a suitable time slot of desired test resources**

If you have found several suitable test resources for your purposes after filtering, you can view all TR calendars at the same time to quickly find a free time slot. Just mark the desired test resources in the *TR overview* and click on **Booking view**. In this view you see all calendars of the selected TRs one below the other. Creating new appointments here is also possible by selecting a suitable time in the calendar.

The monitoring module provides a live status and additional information of all connected <u style="color: blue;">**test resource**</u> s. The connection to **test.guide** is established by the application <u style="color: blue;">**ResourceAdapter**</u> which comes with **test.guide** and which needs to be executed on the respective <u style="color: blue;">**test resource machine**</u>. All provided information are gathered by plug-ins. Typical information are a heartbeat (connection check), system information (CPU, RAM, HDD, ...), execution states, test bench activity and the hard- and software configuration of the test resource machine and the system under test.

All types of test resources are supported. Thus, a test resource can be a huge Hardware-in-the-Loop (HiL) test bench, a node within a container-based cloud infrastructure used for example for Software- or Model-in-the-Loop (SiL/MiL) tests or a local computer of a developer, where also tests are executed.<u style="color: blue;">**workstation**</u> computers, that are used for test data pre- or post-processing (e.g. complex trace analysis), can also be seen as a test resource.info

All provided data from any connected test resource is stored in a separate database and can automatically be linked to test executions stored within the test report management of **test.guide**. This is helpful for comparisons of test executions and reviews of test reports. To use this feature, a test execution info plug-in has to be configured. Further information can be found <u style="color: blue;">below</u>.

<figure>
<img
src="test.guide%20user%20documentation-media/a477518bcf9be13dfe6f69635e87b814c0bb655d.png"
alt="f5d81d6ca01da354d89d695242344c6c_MD5" />
<figcaption
aria-hidden="true">f5d81d6ca01da354d89d695242344c6c_MD5</figcaption>
</figure>

MonitoringOverview

Access to the monitoring features can be restricted by special user permissions, which can be assigned on per-user basis via authentication settings page. Monitoring management permission allows a user to setup monitoring features.info

### 2.3.1. Prerequisites for using the monitoring

First of all the monitoring feature has to be enabled by a server manager by configuring a monitoring database. See also: → <u style="color: blue;">**Monitoring**</u>

A retention period has to be set at the database configuration page. That means, that all data is erased after the configured time period (standard setting is 31 days). Navigate to **Test infrastructure** to set the retention period.error

After activation the monitoring feature, test resources can be connected to **test.guide**.

### 2.3.2. How do I add a new test resource to my test.guide project?

To connect a test resource to **test.guide**, the **ResourceAdapter** must be running on the respective machine, e.g. a control computer of a HiL test bench. An authentication key of a technical user with appropriate permissions (see also <u style="color: blue;">**Project users**</u>) is necessary to operate the **ResourceAdapter**. There are different ways to set up the **ResourceAdapter** that are described below.

**IMPORTANT SAFETY NOTICE**

You are about to install the **test.guide** **ResourceAdapter**. When using **test.guide** test execution, the **ResourceAdapter** enables automated test execution on the respective test bench.

**ATTENTION**: The **ResourceAdapter** must be deactivated when performing manual testing or other manual activities on the test bench. Otherwise, automated testing may be started during such time (which may, for example, affect switches on a terminal automatically). Non-compliance with this safety notice may cause serious bodily harm and damage to property.

Please forward this important safety notice to your company's responsible safety representative. Please also contact this safety representative for any further questions or concerns.

error

There are test resources that consist of more than one node/computer. In general the **ResourceAdapter** should be executed at least on the node where the test automation is running. It is also possible to add more than one node for one test resource to monitor all nodes.info

#### 2.3.2.1. Way 1 (recommended): Preconfigured setup

- Create a technical user and an authentication key for this user (**Project management** and **Manage project user** rights required)
  - Navigate to <u style="color: blue;">**Project users**</u>
  - Click on the dropdown next to **Create new user** located in the upper left corner and then **Create technical user**
  - Fill in at least the required fields
  - Assign the following permissions:
    - **Synchronize ResourceAdapter configuration**
    - **Monitoring data**: **Read** and **Create/Update**
  - Click on **Add user**
  - Find the newly created technical user in the list and click on the dropdown next to **Edit** and then **Show authentication key**
  - Click on **Create key** and follow the dialog to create a new authentication key which needs to be copied before closing the window again
- Create a preconfigured **ResourceAdapter** package
  - Navigate to \*\*\*\*ResourceAdapter\*\* s\*\*
  - Click on **Preconfigure **ResourceAdapter\*\* package\*\* located in the upper right corner
  - Fill in the required fields using the authentication key you copied earlier
  - Choose a template for the new configuration

The first time you create a preconfigured package, you'll have to choose "Example configuration". As soon as there is a **ResourceAdapter** connected, you can also choose the respective configurations as templates.info

- Download the preconfigured package and transfer it to the desired test resource
- Extract the package
- If necessary: Adapt the config file `resourceAdapter.preconfigured.config`

Some plug-ins are configured and activated by default (see also <u style="color: blue;">General information</u>). Others are not. So if you need a special plug-in configuration from beginning, you have to adapt the config file before starting the **ResourceAdapter**. How to do so is explained <u style="color: blue;">here</u>. Configuration changes are of course possible later on.info

- Run the included `starter` script (`.bat` for windows, `.sh` for Linux)

#### 2.3.2.2. Way 2: Manual setup

- Download the **ResourceAdapter**
  - Navigate to **test.guide**
  - In the upper right corner you'll find a button, where you can download a zip archive
  - Download it, transfer it to the desired test resource and extract it
- Adapt the config
  - Open the config file (`resourceAdapter.example.config`)
  - Configure at least all necessary parameters under " **test.guide** Host"
  - Fill in an authentication key of a technical user with appropriate permissions
  - After that you can configure all plug-ins you need
  - Save the config file
- Run the **ResourceAdapter**
  - Start the application by running the included `starter` -script (`.bat` for windows, `.sh` for Linux)

#### 2.3.2.3. Way 3: Running the Resource Adapter in a containerized environment

**test.guide** provides a **ResourceAdapter** container image (base: UBI9-minimal) for running the **ResourceAdapter** in Docker or other container runtimes. The image contains a minimal preconfigured **ResourceAdapter** with only the heartbeat plug-in enabled.

Steps

1.  Download the **ResourceAdapter** container image (e.g. `TEST-GUIDE-ResourceAdapter-1.202.0-ubi9.docker.tar.gz`).
2.  Load it into your container runtime:
    `shell  docker load -i TEST-GUIDE-ResourceAdapter-1.202.0-ubi9.docker.tar.gz`
3.  Start a minimal container:
    `shell  docker run -d --name test.guide-resourceAdapter \    -e TEST_GUIDE_HOST=https://<your_tg_host> \    -e TEST_GUIDE_AUTH_KEY=<auth_key_of_technical_user> \    -e TEST_GUIDE_PROJECT_ID=<project_id> \    -e RESOURCE_LOCATION_ID=<resourceLocationId_of_this_machine> \    tracetronic/resourceadapter-ubi9:1.202.0`

Optional: Provide a custom configuration

Mount your own `resourceAdapter.config` to enable additional plug-ins:

``` shell
-v /path/to/resourceAdapter.config:/home/ra/TTS-TM-ResourcenAdapter/resourceAdapter.config
```

Optional: Use custom certificates / truststore

The recommended way to provide your corporate CA certificates is to build your own image based on the provided one. See below for an example Dockerfile that copies PEM-formatted certificates to the system trust store and updates it.

Example Dockerfile:

    FROM tracetronic/resourceadapter-ubi9:1.202.0

    USER root

    # Copy your internal / corporate root or intermediate CA certificates
    # (one file per certificate, .crt in PEM format)
    COPY corp-root-ca.crt /etc/pki/ca-trust/source/anchors/
    # Add more as needed:
    # COPY another-ca.crt /etc/pki/ca-trust/source/anchors/

    # Update the system trust store (this also regenerates the Java trust store)
    RUN update-ca-trust extract

    USER ra

If building your own image is not an option, you can also mount your certificates and update the trust store at container start:

1.  Create (or extend) a truststore:
    `shell  keytool -importcert \    -file /path/to/certificate.crt \    -alias mycert \    -keystore /path/to/keystore.jks \    -storepass changeit`
2.  Mount the truststore:
    `shell  -v /path/to/keystore.jks:/home/ra/TTS-TM-ResourcenAdapter/keystore.jks`
3.  Let the JVM use it (choose one):
    - Environment variable:
      `shell   -e JAVA_TOOL_OPTIONS="-Djavax.net.ssl.trustStore=/home/ra/TTS-TM-ResourcenAdapter/keystore.jks -Djavax.net.ssl.trustStorePassword=changeit"`
    - Pass JVM args after image name:
      `shell   docker run ... tracetronic/resourceadapter-ubi9:1.202.0 \     -Djavax.net.ssl.trustStore=/home/ra/TTS-TM-ResourcenAdapter/keystore.jks \     -Djavax.net.ssl.trustStorePassword=changeit`

The configured Java truststore affects only the JVM of the **ResourceAdapter**. Processes started by plug-ins (version control clients, execution of python scripts, ...) do not automatically inherit it.

You may need to provide access to your CA certificates for these processes after mounting them in appropriate format.

Examples:

- Git: `-e GIT_SSL_CAINFO=/home/ra/certs/ca-bundle.crt`
- Python requests library: `-e REQUESTS_CA_BUNDLE=/home/ra/certs/ca-bundle.crt`

error

#### 2.3.2.4. General information

- Check, whether the connection is successfully established
  - Navigate in **test.guide** to **IT view**
  - Here the previously connected test resource should be listed in the view
- In both packages, some plug-ins are configured and activated
- To deactivate a plug-in just comment out the respective line by using `#` or `!`
- After the first start a workspace directory is being created
  - If there are no changes in the `starter` script, the workspace directory is located in
    - `%USERPROFILE%/TTS-TM-ResourcenAdapter` for Windows
    - `/home/~user~/TTS-TM-ResourcenAdapter` for Linux
  - In the workspace directory you can find the resulting configuration file `resourceAdapter.config`
  - After the first start, local configuration changes has to be done in the resulting configuration file named above
  - Changes in the `resourceAdapter.preconfigured.config` or `resourceAdapter.example.config` will not be taken into account anymore after first start of the **ResourceAdapter** and as long as a workspace exists
  - Logs are also available in this directory

You can change the workspace directory by editing the `starter` script. Just set the parameter `CONFIG_DIR` to the desired path.lightbulb_2

Due to technical reasons, the "AutoUpdate" functionality provided by the **ResourceAdapter** can only update the **ResourceAdapter** application itself and the included plug-ins. The necessary `bootstrap.jar` file and especially the included Java Runtime Environment (JRE) cannot be updated automatically.

Please refer to the `ResourceAdapterUpdateReadme.txt` in the extracted installation package or the **ResourceAdapter** installation folder for further details and manual update steps! If the effort for the manual update of the included JRE is too high, please use your own JRE.

error

### 2.3.3. How can I change existing ResourceAdapter configurations...

Configuration changes of a test resource already connected can be done both within the **test.guide** web UI and in the configuration file locally on the connected test resource. The configuration is key-value based. You can find all possible keys in the `resourceAdapter.example.config` file, located in the `.zip` -File.

Because of the two ways to edit the configuration, **test.guide** validates the configuration file by a hash. That is why all comments are removed within the resulting configuration file.info

#### 2.3.3.1. ... via the test.guide web UI?

- Navigate to \*\*\*\*ResourceAdapter\*\* s\*\*

- Here you can configure one or more existing **ResourceAdapter** configurations

- First of all, you need to select the desired configuration(s) in the section **Configure **ResourceAdapter\*\* s\*\*

  - If you have a large amount of test resources connected, use the filter field to find the desired **ResourceAdapter** s
  - Select all filter results or only a specific one
  - On the right side you see your selection

- To edit the selected configurations use the **Edit configurations**

- The first column contains all existing keys, the concrete values of the respective configurations are listed in the following columns

- Find out the key you want to change and edit the value for the desired **ResourceAdapter** in the matching column on the right side by clicking into the respective cell

- Bulk changes are also possible by using the small pen-button on the right side within the key-cell

- A restart of the affected **ResourceAdapter** s will be performed automatically

Please be aware, that the **ResourceAdapter** s on test resources that have been changed are restarted automatically after hitting **Save configuration**. If there is an automated test execution via the **ResourceAdapter** actually running on an updated node, this might lead to problems.error

In a bulk change only visible columns are edited. If you want to change only a few configurations, hide the columns you don't want to change beforehand.lightbulb_2

#### 2.3.3.2. ... by editing the configuration file locally?

- To change the configuration of an existing test resource locally please edit the `resourceAdapter.config` within the workspace directory
- A manual restart of the **ResourceAdapter** is required

### 2.3.4. How do I add/configure a new ResourceAdapter plug-in?

Every plug-in needs to be initialized and configured properly. The syntax is as followed:

`plugin.[internal plug-in name].[instance].config.[parameter/property]`

- `[internal plug-in name]`: Internal name of the plug-in
- `[instance]`: Unique number of the instance, because a plug-in can be instantiated multiple times
- `[parameter/property]`: There are some default parameters for all plug-ins and some special parameters for single plug-ins, called `properties`

All possible parameters and properties can be found in the `resourceAdapter.example.config`.

To add a new plug-in you just need to edit the **configuration file** of the desired **ResourceAdapter** as described above. Please refer to the `resourceAdapter.example.config` file, that can be found in the extracted installation package. It is recommended to just copy and paste the respective lines and fill in the needed values.

In the **web UI** you can also add new rows by clicking on **Add row**. Make sure to insert the whole path of the desired key, e.g. `plugin.de.tracetronic.ttstm.monitoring.plugin.heartbeat.HeartBeatPlugin.1.config.polling`. After adding a key, you can add the value(s) as described above. If you add more than one key for a plug-in, **test.guide** will automatically group them.

### 2.3.5. How do I use test resource monitoring data?

All monitoring information can be found in the monitoring menu. There are **different views** for different use cases. In addition to the views, which all mainly focus on the test resources, monitoring details can also be **linked to test results automatically**. This is very helpful for evaluating test results.

#### 2.3.5.1. How do I get a quick overview over all my test resources?

To get a quick overview over all connected test resources, navigate to **IT view**. Here you can find all connected test resources and status information of these, e.g. vital data of a node such as CPU and RAM usage. By using thresholds vital data is evaluated. There are distinct thresholds for serious and critical values. Values can be configured in the **ResourceAdapter** setup. The state of the entire node is evaluated using the worst single value state.

All test resources are sorted by their location and the respective test resource name. The full location path is displayed at the top. By clicking on a lower location level (the row beneath) only test resources matching this location are displayed. The view of a test resource shows the health state (provided by the TestbenchHealth Plug-in) on the top left, the test resource name in the middle and the by thresholds interpreted vital data of the test resource on the right. Below that, the current action is shown. As long as there is no active test execution, in the lower line on the right you can find an icon indicating whether there is a manual user activity on the test resource.

The view of a test resource depends on the configured plug-ins. Hence, a test resource where no user activity plug-in is configured will not show the button for user activity.info

As soon as a test was startet, different information about the current test run is displayed. This can be for example the test project, test suite and test case name. The test execution status is also shown at the executing test resource. Therefore, the icon in the bottom line is hidden to show the established time and the number of finished test cases.

By clicking on a test resource name you'll get a detail view of the selected test resource with all information provided by the configured plug-ins.

#### 2.3.5.2. Can I find out, what activities were ongoing on my test resources?

Yes, by using the Activity view. Navigate to **Activity** where you can filter test resources by their location and after that by their name.

To provide wildcard filtering on both levels, location and test resource name, it is not possible to start filtering by the test resource name. When you don't know the location of your test resource, use the wildcard `*` to see all available locations.lightbulb_2

Beneath the test resource filter you can also use time filters to show only a desired period of time.

After filling in the filter parameters, click on **Filter** to see the filtered results. On the bottom you now can see the activity distribution.

In the top right corner of the distribution area of the activity view you can find a possibility to export the shown data to Excel. Exporting is also possible by using the API. See [Monitoring API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Monitoring%20API) for further information.lightbulb_2

##### 2.3.5.2.1. How to set up (custom) test resource machine activities?

Please be aware that there is the <u style="color: blue;">**TRM activity**</u> (<u style="color: blue;">more details</u>) on the one hand and the <u style="color: blue;">**TRM state**</u> (<u style="color: blue;">more details</u>) on the other hand. Activity refers to things going on at the test resource machine. The state of a test resource machine contains information about the system health or parts of that.error

There are five activity types configured by default:

1.  Offline
2.  Idle
3.  User activity
4.  CI activity
5.  Automated test execution

Every activity type has an ID, a name, a priority and a color. You can add additional activity types and give them a name, priority and color at **Settings**. The ID will be assigned automatically. It is also possible to change the attributes of existing activity types.

The deletion of activity types is not possible because this could cause gaps within the activity distribution of test resources. Furthermore, it is not recommended to change the five default activity types shown in the picture above because there are several mechanisms in **test.guide** that assume that these are set as in the default.error

Test resource activities are set by some plug-ins within the **ResourceAdapter**. For all plug-ins, that set the test resource activity, the `resourceAdapter.example.config` contains a suggestion for the activity type ID. The suggested activity type ID can be changed in the **ResourceAdapter** configuration. Please watch out for the property `testBenchActivityType` within the plug-in configuration. The most powerful and flexible plug-in for setting test resource activities is the **Test Bench Activity REST API Plug-in**, that provides a REST-API endpoint on the machine, where the **ResourceAdapter** is running. The user can set every configured activity by using simple `POST` requests. Moreover, optional information can be provided by the user as well.

For more information, please refer to the `resourceAdapter.example.config` file, that can be found in the extracted **ResourceAdapter** installation package.

Because of the multiple opportunities to set an activity, the priority of an activity type is necessary. The higher the priority the more important is an activity. That means if there are overlapping activities, only the one with the highest priority will be displayed in the activity view.

#### 2.3.5.3. How can I find out what test resource configuration was active during my test run?

**test.guide** can link monitoring details such as configuration information to test reports uploaded to **test.guide** automatically. Therefore, the **ResourceAdapter** has to be running during the test execution and a test execution info plug-in must be configured. For EXAM this only works, when the parameter `createAtxTestReport` is set to `true` configured in the EXAM test execution info plug-in.

In the standard **ResourceAdapter** configuration, the ecu.test test execution info plug-in is already activated.lightbulb_2

After the activation you can find monitoring details in the <u style="color: blue;">detail view of test reports</u> on the bottom. You can use the provided information e.g. for comparisons of test runs to find out whether a configuration change caused a changing test result.

#### 2.3.5.4. How to use the aggregated overall state of a test resource?

Please be aware that there is the <u style="color: blue;">**TRM activity**</u> (<u style="color: blue;">more details</u>) on the one hand and the <u style="color: blue;">**TRM state**</u> (<u style="color: blue;">more details</u>) on the other hand. Activity refers to things going on at the test resource machine. The state of a test resource machine contains information about the system health or parts of that.error

The aggregated test resource state aggregates all state information of a test resource. The information of connection state (gathered by the Heart-Beat Plug-in), monitoring state (gathered by different monitoring plug-ins, e.g. CPU Load Plug-in) and the component state (provided by the TestbenchHealth Plug-in, the Jenkins Agent Plug-in and the Execution Plug-in) are taken into account for the aggregated state of a test resource.

Currently, all state information are used for displaying purposes only. It is planned for the future to use state information for controlling workflows, e.g. in automated test execution, as well.info

There are six states, which are shown in ascending order of severity in the following table.

| State | Meaning | Possible reasons |
|----|----|----|
| Unknown | the state could not be determined | there are some information missing, e.g. due to missing configuration of plug-ins |
| OK | everything is ok | none of the configured plug-ins reported a problem |
| Warning | a non-critical problem has occurred | there is an overrun of a yellow threshold of a monitoring plug-in |
| Not available | the test resource is not available for automated test execution | a manual interaction is in progress and/or an executor plug-in is in pause mode |
| Critical | a critical problem has occurred | a problem was reported at at least one component state and/or there is an overrun of a red threshold of a monitoring plug-in |
| Offline | there is no connection of the respective **ResourceAdapter** to **test.guide** | no heartbeats sent by the Heart-Beat Plug-in |

Details about the state-affecting values of the individual plug-ins can be found on the respective test resource detail page.

##### 2.3.5.4.1. Mapping of single (component) states to the aggregated test resource state

**Connection state (Heart-Beat Plug-in)**

The connection between a **ResourceAdapter** and **test.guide** is a one-way polling connection. This means that the **ResourceAdapter** sends data to **test.guide** at cyclic intervals. To signal the availability of the test resource to **test.guide**, the **ResourceAdapter** sends so-called heartbeats with the aid of the Heart-Beat plug-in. If the heartbeats do not occur for a certain time, it is assumed that the respective **ResourceAdapter** no longer has a connection to **test.guide** and is therefore "offline". This can mean that there is a problem with the network connection or that the **ResourceAdapter** is simply not running on the respective host system.

| Connection state (Heart-Beat Plug-in) | Mapped aggregated test resource state |
|----|----|
| No known connection state (Heart-Beat Plug-in is not activated (no active configuration exists in the **ResourceAdapter**) - **Not recommended!**) | Unknown |
| **ResourceAdapter** is online and connected to **test.guide** (Heart-Beat Plug-in sends heartbeats) | any other state not shown in this table |
| **ResourceAdapter** is offline and not connected to **test.guide** (no heartbeats are sent by Heart-Beat Plug-in) | Offline |

**Monitoring state**

There are different plug-ins gathering system information and compare it with thresholds (green, yellow, red). The thresholds can be defined in the plug-in configurations. The following plug-ins are monitoring plug-ins:

- CPU Load Plug-in
- CPU Load Per Process Plug-in
- RAM Usage Plug-in
- RAM Usage Per Process Plug-in
- HDD Usage Plug-in
- Network Traffic Plug-in
- Network Adapter Plug-in

In addition to this list, there is the **test.guide** Report Upload Plug-in, which also has a built-in monitoring, that can optionally be enabled.

| Monitoring state | Mapped aggregated test resource state |
|----|----|
| Grey: occurs e.g. if a monitored process is not running (depends on plug-in configuration) | Unknown |
| Green: no yellow threshold is exceeded in the configured monitoring plug-ins | OK |
| Yellow: at least one yellow threshold is exceeded in the configured monitoring plug-ins | Warning |
| Red: at least one red threshold is exceeded in the configured monitoring plug-ins | Critical |

**Component state**

Users can set custom component states by using the TestbenchHealth Plug-in. The main use case for this plug-in is reporting automatic healing processes at the test resources to **test.guide**. Further information about the plug-in can be found in the `resourceAdapter.example.config`.

| TestbenchHealth Plug-in information | Component state | Mapped aggregated test resource state |
|----|----|----|
| default value | INSUFFICIENT_DATA | Unknown |
| user set component state to "fixed" | INTERVENTION_SUCCESSFUL | OK |
| user set component state to "error", which could mean that an automatic healing is in progress | ACTION_IN_PROGRESS | Not available |
| user set component state to "broken", which could mean that all automatic healing attempts have failed and a manual interaction is now necessary to fix the problem | MANUAL_ACTION_NECESSARY | Critical |

In addition to the TestbenchHealth Plug-in, plug-ins used to make the respective test resource an executor also report information about their state to **test.guide** using the component state. These plug-ins are the **Jenkins Agent Plug-in**, the **Execution Plug-in**, and the **FlowAutomation Plug-in**.

| Plug-in information | Component state | Mapped aggregated test resource state |
|----|----|----|
| **Jenkins Agent Plug-in**: No connection to Jenkins controller with no additional information about the reason (e.g. during an initialization) **Execution Plug-in**: The test resource is not ready for executing an execution task due to configuration restraints (e.g. ecu.test is running) **FlowAutomation Plug-in**: - | INSUFFICIENT_DATA | Unknown |
| **Jenkins Agent Plug-in**: The executor is ready to receive a job or a job is currently being executed **Execution Plug-in**: The executor is ready to receive an execution task or an execution task is currently being executed **FlowAutomation Plug-in**: The FlowAutomation Plug-in is ready to receive a flow task or a flow task is currently being executed | OK | OK |
| **Jenkins Agent Plug-in**: The agent is being restarted (e.g. due to a restart of Jenkins controller) **Execution Plug-in**: - **FlowAutomation Plug-in**: - | ACTION_IN_PROGRESS | Not available |
| **Jenkins Agent Plug-in**: The agent (executor) is temporarily set offline by the user, the agent is still connected to Jenkins controller **Execution Plug-in**: The executor is manually set offline by the user **FlowAutomation Plug-in**: - | OFFLINE (EXECUTOR_OFFLINE) | Not available |
| **Jenkins Agent Plug-in**: The agent (executor) has been disconnected by the user **Execution Plug-in**: The executor has no connection to **test.guide** **FlowAutomation Plug-in**: - | DISCONNECTED (EXECUTOR_DISCONNECTED) | Critical |
| **Jenkins Agent Plug-in**: Connection to the Jenkins controller is not possible (e.g. due to a not matching token) **Execution Plug-in**: The Execution Plug-in has crashed **FlowAutomation Plug-in**: The FlowAutomation Plug-in has crashed | CRASHED | Critical |
| **Jenkins Agent Plug-in**: There is a configuration error, the initialization was not successful or the Jenkins controller is offline **Execution Plug-in**: - **FlowAutomation Plug-in**: The ResourceAdapter user is missing the FLOW_TASK_EXECUTE permission in test.guide | MANUAL_ACTION_NECESSARY | Critical |

The state of a single component is displayed by an icon in the panel "Component state" on the respective test resource detail page. The name of the state is shown on mouseover.lightbulb_2

## 2.4. Using the artifact management

The **test.guide** artifact management enables the uniform handling of all files which are required during the testing process. The test artifacts are physically stored on existing file shares in the customer's infrastructure. For these purpose, the **test.guide** artifact management provides connections to various external storage systems:

- SMB (Server Message Block) servers
- SFTP (Secure File Transfer Protocol) servers
- jFrog Artifactory servers
- Simple Storage Services (AWS S3)
- Azure Blob Storages
- Local file systems on the test.guide server (intended for testing purposes only)

Test artifacts can be uploaded, downloaded, shared and deleted via **test.guide**.

### 2.4.1. Depositories

Artifacts are organized in depositories. One depository should contain all artifacts that are to be treated equally during the testing process. This means that the same user groups will have the same access rights to all artifacts in the depository. Several storages can be connected to a depository, but only one can be active at a time.

#### 2.4.1.1. How do I set up a depository?

1.  Create a depository and configure a storage connection.
    1.  Navigate to the page *Artifact Management \> Depositories* and create a new depository via the button *Add depository*. Enter a depository name and a depository ID and save the depository via the button *Save*.
    2.  Navigate to the depository detail page by clicking on the depository name. Create a new storage connection via the button *Add storage*.
    3.  Select the desired storage type, enter a storage name and configure the connection settings.
    4.  Verify the entered connection settings via the buttons *Test connection* and *Start*. If the connection is successful save the storage connection via the button *Save*.
    5.  Activate the storage connection via the action *Activate*.
2.  Configure project role permissions for the depository.
    1.  If not already done: Navigate to the page *Project settings \> Project roles* and create project roles for all user groups that should interact with the depository via the button *Create project role*. Enter a project role name and save the depository via the button *Save*. You don't need to assign any permissions at this point.
    2.  If not already done: Assign members to the created project roles via the action *Manage members*. Press the *Add user* button, select all users that should have the same permissions on the depository and add them via the button *Add*.
    3.  Navigate back to the depository detail page via the page *Artifact Management \> Depositories \> <depository name>*. Assign the created project roles to permissions via the button *Add permissions* in the *Permissions for project roles* section. Select the desired project role, assign the required permissions via the checkboxes and save via the button *Save*.

Your depository is now set up and can be used by users with the configured project roles.

## 2.5. Using the test execution

The **test.guide** **test execution** enables a **distributed processing of tests** on the test benches connected to **test.guide**. The so-called test execution tasks can be prioritized and are sorted in a queue according to priority first and creation date second. Queued test execution tasks can be renamed, reprioritized, aborted or deleted.

Playbooks can be used as an instrument to plan test executions. Multiple times one or more test execution tasks can be generated from a playbook. You can get a short introduction into the basic concepts of the automated test execution and playbooks with the following videos:

Click here for introduction videos.
![](https://www.youtube.com/watch?v=HyDZ_phuPjA)
![](https://www.youtube.com/watch?v=cOYgyr6_yaE)

There are also 4 advanced videos which explain the concepts and possibilities of the automated test execution with playbooks in more detail:

Click here for advanced videos.
![](https://www.youtube.com/watch?v=bzlhhzSSiNY)
![](https://www.youtube.com/watch?v=um3JIkXRZAc)
![](https://www.youtube.com/watch?v=gjYIVRfGfpQ)
![](https://www.youtube.com/watch?v=IIUFAwPjifw)

### 2.5.1. Requirements

In any case the **Execution Plug-in** in the **ResourceAdapter** has to be activated and configured properly. See <u style="color: blue;">**ResourceAdapter** plug-in configuration</u> for more details and please refer to the `resourceAdapter.example.config` file, that can be found in the extracted **ResourceAdapter** package.

The plug-in is not activated by default because the necessary parameter `ecutest.executable` is dependent of the installation path of ecu.test. Thus, the parameter can not have an initial generic value.info

To use the test execution feature without Jenkins, a test bench needs to have **ecu.test 2020.3 or newer** installed together with the **test.guide** **ResourceAdapter**.

### 2.5.2. Execution tasks

#### 2.5.2.1. What is a test bundle?

We distinguish between direct test execution with ecu.test, test execution via user defined Jenkins jobs and generic task execution.

The direct test execution **with ecu.test** supports multiple types of test bundles:

- single ecu.test packages
- single ecu.test projects
- whole ecu.test workspaces (zipped or as folder) and
- archived ecu.test projects (in ecu.test → right-click on the project file → Export project... → as archive...)

Test bundles which are executed **with user defined Jenkins jobs** are freely designable.The job has to take care of the execution itself, including starting and stopping ecu.test (or another test tool) and uploading test reports to **test.guide**.

For the generic execution of tasks an arbitrary workspace needs to be specified. Within this workspace specified commands will be executed.

Test bundles can either be managed outside **test.guide** and provided by reference (see `"location"` and `"scm"` in the next section). Or test bundles can be uploaded to the artifact management and used from there (see `"artifact"` in the next section).

#### 2.5.2.2. How do I create execution tasks via file upload?

Execution tasks can be created via " **Upload execution tasks** " under **Tasks**. There you can upload a **JSON file** (\*.json) to **test.guide** that describes the execution task.The file must at least contain the following information:

- `"name"` - a freely selectable **name** of the execution task
- `"priority"` - the **priority** of the task as a whole number between 0 (lowest) and 100 (highest)
- `"source"` - the specification of the test bundle **source**
- `"xilConfigRequirements"` - a list of all **requirements** that a test bench must fulfil to execute the task

The **test bundle source** has to be one of the following options:

- **location** - defines a path to a test bundle that is accessible on the test bench and has the following JSON data:
  - `"sourceType"` - needs to be set to `"location"`
  - `"path"` - the **path** to the test bundle, either on a network or a local drive
- **artifact** - defines the **ID of the test bundle artifact** in the **test.guide** artifact management and has the following JSON data:
  - `"sourceType"` - needs to be set to `"artifact"`
  - `"artifactId"` - the **ID of the test bundle artifact** in the format `"<depository ID>-<number>"`
- **scm** - defines the path and version of a test bundle in a source control management tool and has the following JSON data:
  - `"sourceType"` - needs to be set to `"scm"`
  - `"scmLabel"` - label of the previously integrated SCM tool (if specified, `"scmUrl"` is not allowed!)
  - `"scmUrl"` - url of the previously integrated SCM tool (if specified, `"scmLabel"` is not allowed!)
  - `"scmCommit"` - if Git: a **commit hash**, **branch name** or **tag**; if SVN: a **commit number** or " **HEAD** " for the latest commit

If you use a Git repository as a source, the test bench must have Git installed in a version of **2.10 or newer**. Otherwise, a JGit client will be used as fallback (not recommended for performance reasons). You can also explicitly configure the used Git client in the `resourceAdapter.config` file: `plugin.de.tracetronic.ttstm.monitoring.plugin.execution.ExecutionPlugin.1.config.properties.gitClient=git` or `=jgit`.info

SCM clone and checkout operations are tried several times before the error is passed to test.guide. This is to bypass sporadic errors at the test bench.info

The scheme of a test bundle's requirement corresponds to that of a configuration property of a test bench from the Monitoring section. A requirement is therefore a triple with:

- `"label"` - the **identifier** of the configuration property
- `"category"` - the **category** of the configuration property
- `"value"` - the **value** to be matched of the configuration property

Optionally, there can also be details:

- `"details"` - the list of **details** to be checked against the configuration property (a detail again consists of `"label"`, `"category"` and `"value"`)

In all of these fields you can use the wildcards `*` (matching multiple characters) and `?` (matching exactly one character).

You can find additional setting options, such as workspace dependencies, user-defined parameters or playbooks, in the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

After pressing the " **Create execution task** " button, an execution task is created and queued according to its priority.

#### 2.5.2.3. How do I create execution tasks for delayed or recurring execution?

When uploading execution tasks via " **Upload execution tasks** " under **Tasks**, the type of the tasks can also be specified. In addition to immediate one-time execution, a task may be scheduled as delayed one-time execution or recurring execution.

If you select the delayed one-time execution, a project job will be created which generates one execution task at a certain time. You have to specify the time of the execution task creation.

If you select the recurring execution, a project job will be created which generates new execution tasks at times that match a certain cron expression in the [UNIX format](https://man7.org/linux/man-pages/man5/crontab.5.html). Additionally, you may specify a time of first execution of this recurring task. However, note that this may not be the actual first time of creation of the task. The first execution time will be moved to the first timestamp matching the specified cron expression after the specified time. If `Check last execution` is enabled, the recurring job will check if the last execution tasks created by this job are already finished. Otherwise, no new execution tasks will be created.

You can find and manage all project jobs under **Manage jobs**.

#### 2.5.2.4. Can I also assign execution tasks directly to test benches?

Yes, this is possible.If the **test.guide** **ResourceAdapter** of a test bench has been correctly configured for test execution, the test bench automatically gets the following configuration property:

- **Category**: `XIL`
- **Label**: `Identifier`
- **Value**: resource location ID of the test bench

You can reference this configuration in the execution task XIL configuration requirements:

    "xilConfigRequirements": [{
        "category": "XIL",
        "label": "Identifier",
        "value": "<resource location ID of the test bench>"
    }]

#### 2.5.2.5. How do I create execution tasks through artifacts?

When using the test execution with ecu.test, it is possible to create execution tasks through test bundle sources uploaded to the artifact management. All uploaded artifacts that have the attribute " **ArtifactType** " set to one of the following values can be used for creating execution tasks:

- " **Workspace** " - zipped ecu.test workspace or
- " **ProjectArchive** " - archived ecu.test project

To assign the artifact to a certain test bench (or a group of test benches), an additional attribute " **RequiredXilType** " can be added. In this case, the test bundle will only be executed on test benches with the following configuration property:

- **Category**: `XIL`
- **Label**: `Type`
- **Value**: value of attribute RequiredXilType

You can reference this configuration in the execution task XIL configuration requirements:

    "xilConfigRequirements": [{
        "category": "XIL",
        "label": "Type",
        "value": "<value of RequiredXilType>"
    }]

Creating an execution task through an artifact can either be triggered by clicking the **Rerun as execution task** on an artifact's details page or by clicking the corresponding menu entry on the page **Artifacts**.

Doing so brings up a new window. After pressing the "Create" button, an execution task is created and queued according to its priority. Furthermore, for every of these execution tasks a release coverage will be created.

**User-defined parameters** can be used to filter your execution tasks on the **Tasks** page. They are also available during the execution. See also <u style="color: blue;">task parameters in Jenkins pipelines</u>, <u style="color: blue;">task parameters in ecu.test</u> and <u style="color: blue;">task parameters during playbook execution</u>.info

#### 2.5.2.6. How can execution tasks reference artifacts that are not part of the workspace?

Execution tasks can contain a `"dependencies"` section. Workspace dependencies reference sources that are not part of the workspace source itself but are required for the execution.

As a source for a workspace dependency you can provide an artifact in the **test.guide** artifact management, an SCM repository or an HTTP link to a file (e.g. in the **test.guide** file storage). You can specify whether the artifact shall be additionally copied to a local path on the test bench or whether it shall be unzipped (if the dependency references a zipped folder).

In the JSON description dependencies could look like the following:

    "dependencies": [
        {
            "label": "A2L",
            "source": {
                "sourceType": "artifact",
                "artifactId": "mydepot-123"
            }
        },
        {
            "label": "TRACES",
            "source": {
                "sourceType": "link",
                "link": "http://link/in/file/storage"
            },
            "unzip": true,
            "copyTo": "local/file/path"
        }
    ]

The dependency source has to be one of the following options:

- **Artifact** - defines the **ID of an artifact** in the **test.guide** artifact management and has the following JSON data:
  - `"sourceType"` - needs to be set to `"artifact"`
  - `"artifactId"` - the ID of the artifact in the format `"<depository ID>-<number>"`
- **SCM** - defines the path and version of a repository in a source control management tool and has the following JSON data:
  - `"sourceType"` - needs to be set to `"scm"`
  - `"scmLabel"` - label of the previously integrated SCM tool
  - `"scmCommit"` - if Git: a **commit hash**, **branch name** or **tag**; if SVN: a **commit number** or " **HEAD** " for the latest commit
- **Link** - defines the **HTTP link to a file** (e.g. in the **test.guide** file storage) and has the following JSON data:
  - `"sourceType"` - needs to be set to `"link"`
  - `"link"` - a hyperlink to the referenced resource, e.g. `https://example.com/resource.zip`

If you want to use the same SCM repository with different commit hashes, branch names or tags in different dependencies you need to use the `copyTo` option in each dependency that uses this SCM repository. Furthermore, it is not allowed to specify the same SCM repository in the dependencies, that is already used as `source` SCM of the task or playbook.

Workspace dependency labels can be referenced with the notation `${LABEL}` in some places of playbook. See <u style="color: blue;">variables replacement in playbooks</u> for more information. At the beginning of an execution, the referenced labels will be replaced with the actual absolute paths of the workspace dependencies.info

If you use the <u style="color: blue;">execution with Jenkins</u> together with workspace dependencies, the dependencies will be available as build parameters in the Jenkins job. The dependency label will be given as parameter name and the path of the provided dependency will be given as parameter value.info

You can find a more detailed description of the workspace dependencies schema in the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

#### 2.5.2.7. Where can I see, edit and delete execution tasks?

The page under **Tasks** provides an overview of all created execution tasks.

Each task can be downloaded, deleted or rescheduled. Furthermore, not yet started execution tasks can be edited or re-prioritized. Finished execution tasks provide a link to their test results.

It is also possible to filter execution tasks by their properties. The filter form can be used to create the filter.

The filter connects multiple entries for the same property using the logical OR operation while entries in different properties are connected using the logical AND operation.info

In addition to the user interface on the page, a filter may be provided using URL page parameters. The following table gives an overview of filterable properties and their respective parameter keys that can be used in the page parameters.

| Execution task property (as in JSON) | Parameter key | Note |
|----|----|----|
| name | `taskName` |  |
| matchingXils | `matchingXil` |  |
| state | `state` | Provide the state in capital letters (e.g. `BLOCKED`, `WAITING`, ...) |
| taskId | `taskId` |  |
| uploadUser.userName | `uploadUser` |  |
| source.artifactId | `artifactId` | Only for execution tasks with source type `"artifact"`. |
| source.scmLabel | `scmTool` | Only for execution tasks with source type `"scm"`. |
| source.scmCommit | `scmReference` | Only for execution tasks with source type `"scm"`. |
| source.path | `location` | Only for execution tasks with source type `"location"`. |
| playbook.playbookId | `playbookId` |  |
| parameters | `parameter` | Provide the key and value you want to filter by using the `[key]value` syntax. |
| attributes | `attribute` | Provide the key and value you want to filter by using the `[key]value` syntax. |
| priority | `priorityMin` and `priorityMax` | Provide the lower bound (`priorityMin`) and/or the upper bound (`priorityMax`) for the priority. |
| creationDate | `createdAfter` and `createdBefore` | Provide the lower bound (`createdAfter`) and/or the upper bound (`createdBefore`) for the creation date. The provided date expression will be evaluated using the timezone of the browser. Examples (make sure to URL encode the expression): - `now + 2d` (current timestamp +2 days) - `now - 7y` (current timestamp -7 years) - `today 19:00` (current day 19:00) - `today 19:00 - 1d` (yesterday 19:00) - `23.04.2012` - `23.04.2012 16:55` - `23.04.2012 04:55 PM` (12-hour-system) - `04/ 23/ 2012 16:55` (month-year-day format) - `23.04.2012 16:55 - 7h` (-7 hours) - `23.04.2012 16:55 + 7min` (+7 minutes) - `23.04.2012 16:55 - 2d` (-2 days) - `23.04.2012 16:55 - 2w` (-2 weeks) - `23.04.2012 16:55 - 2m` (-2 months) - `23.04.2012 16:55 - 2y` (-2 years) |

Example: Assume you want to filter for all execution tasks that have the name "My task" and the state "finished". The according URL looks like the following:

    <test-guide-base-url>/execution/overview?taskName=My+task&state=FINISHED

If you want to provide multiple entries for the same property, just specify the page parameter multiple times:

    <test-guide-base-url>/execution/overview?taskName=My+task&taskName=Your+task

Using this query, the page will show all execution tasks that have the name "My task" or "Your task".

You may need to properly escape special characters in URLs. For example spaces may be inserted using `+` or `%20` while slashes (e.g. in order to filter on the matchingXils property) can be escaped by `%2F`.info

#### 2.5.2.8. What are the different states of the tasks about?

After creating an execution task, all currently suitable test benches will be calculated based on the tasks XIL configuration requirements, and a corresponding state will be set. The following states are possible:

- **blocked**: There is currently no test bench that meets the requirements.
- **waiting**: There are one or more suitable test benches, but they are currently occupied.
- **running**: The task is currently being executed on a suitable test bench.
- **finished**: The execution of the task on a suitable test bench has successfully completed.
- **failed**: An error has occurred while executing the task on a test bench.
- **unknown**: The current state of the task could not be determined.

If the configuration of a test bench changes, the states and suitable test benches of all execution tasks are recalculated automatically.

**Please note the mandatory order of events: Set test bench offline → Change test bench configuration → Set test bench online.**info

#### 2.5.2.9. How can I abort an execution task?

There are two different ways to abort an execution task.

During the execution of an execution task the **ResourceAdapter** offers a context menu entry to abort the execution task. Using the respective button leads to an immediate abort of the task. The currently running test step will be aborted, no teardown will be executed and **ecu.test** will not be shutdown. If the execution plugin of the **ResourceAdapter** uses an automation strategy that is not blocked by a running **ecu.test**, it might be helpful to first take the execution plugin offline and then aborting the execution task.

- Via **test.guide**.

In the overview page of execution tasks as well as in the details page of an execution task there is an action that aborts the task. If the task is not yet running, the task is immediately set to the error state and assigned with an error message. If the task is currently executed on any test bench, the task is marked accordingly and will be aborted soon. Aborting a task via **test.guide** will abort the current test case and continue with the teardown block. If the teardown block is already executing the abort request will be ignored and the task will be finished normally.

Both abort strategies do only effect the execution if the executing dispatcher of the execution plugin is the **ecu.test** dispatcher or the generic dispatcher. Aborting tasks using the Jenkins dispatcher is not yet supported.

#### 2.5.2.10. Can I set an expiration date for an execution task?

In the `additionalSettings` section of an execution task it is possible to specify the `expirationTimeInMinutes` field. If not specified the execution task will wait infinitely until its execution is finally started on a matching test bench. If the expiration time is set, the execution task will be set to the error state after the specified time if the task has not been started yet.

Example of an execution task with an expiration time of 6 hours:

    {
      "name" : "My Task",
      ...
      "additionalSettings" : {
        "expirationTimeInMinutes" : 360,
        ...
      }
    }

#### 2.5.2.11. Can I also create, delete, and edit execution tasks programmatically?

In addition to the control via the graphical user interface, a **REST API** is provided for all important functionalities of the execution distribution. The documentation of the API and examples for the JSON files described above can be found at the following link: [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

### 2.5.3. Execution with ecu.test

#### 2.5.3.1. How does the task execution work directly with ecu.test?

You can execute your execution tasks directly with ecu.test. The **ResourceAdapter** then executes the task on the test bench using the configured ecu.test and automatically uploads the test results to test.guide.

All **user-defined parameters** of the execution task are available as constants in ecu.test during the execution. See <u style="color: blue;">details about constants in ecu.test during execution</u> for more information.info

#### 2.5.3.2. How should I configure the Resource Adapter for the Execution with ecu.test?

The test bench needs to have an ecu.test installed and the **test.guide** **ResourceAdapter** started. An ecu.test process must not be running, otherwise the test bench will be considered busy and does not accept new tasks. The following **ResourceAdapter** plugins have to be configured:

- **Execution-Plugin**
- **ecu.test-TestExecutionInfo-Plugin**

Example configurations for each plugin can be found in **ResourceAdapter** example config.

#### 2.5.3.3. How can I set up the ResourceAdapter to use multiple versions of ecu.test?

Referring to the <u style="color: blue;">requirements for the test execution</u>, it is necessary to configure a path to an ecu.test executable using the `ecutest.executable` property of the executable plugin.

If there are multiple versions of ecu.test installed on the test bench you can configure these versions in the **ResourceAdapter** config using labels (for example `ecutest.executable.<myLabel> = path/to/executable`). See the **ResourceAdapter** example config for an explicit example.

For each label configured in this way, the following configuration property is sent to **test.guide**:

- **Category**: `XIL/ecu.test`
- **Label**: label of the ecu.test installation (`<myLabel>`)
- **Value**: path to the ecu.test executable (`path/to/executable`)

If you want to use one specific of the configured ecu.test versions for task execution, you can add an entry to the XIL configuration requirements of the execution task (or playbook). You can use the `*` wildcard for the `"value"` field as the ecu.test executable may be installed in different locations on different test benches:

    "xilConfigRequirements": [{
        "category": "XIL/ecu.test",
        "label": "<myLabel>",
        "value": "*"
    }]

See <u style="color: blue;">XIL configuration requirements in test bundles</u> for more information.

At most one XIL configuration requirement with `"category": "XIL/ecu.test"` per execution task (or playbook) is allowed. If none is specified the default executable (given at `ecutest.executable` in the **ResourceAdapter** config) will be used.error

### 2.5.4. Execution with Jenkins

#### 2.5.4.1. How does the task execution work with Jenkins?

The execution via Jenkins is based on **Jenkins jobs**, which have to be preconfigured by the user. The connection to Jenkins can be configured in the **ResourceAdapter** of the respective test benches (see sample configuration of the **ResourceAdapter**). Each execution task is linked to an executable test bundle, which is located on a network drive, in the **test.guide** artifact management or in a source control management tool. The design of the test bundles is therefore completely arbitrary and depends only on their executability in the job. Following three parameters are passed to Jenkins job builds:

- `"taskId"` - the ID of the corresponding execution task in **test.guide**
- `"location"` - the path to the test bundle located on a network drive or path to the downloaded artifact
- `"agentName"` - the name of the Jenkins agent running on the same PC as the accessed **ResourceAdapter**

Additionally, all **workspace dependencies** and all **user-defined parameters** of the execution task will be provided as build parameters to the Jenkins job. User-defined parameters overwrite workspace dependencies and workspace dependencies overwrite `"taskId"`, `"location"` and `"agentName"`.info

If you want to upload test reports to **test.guide** it is important to set the additional constant **TT_TASK_ID** to the value of `"taskId"` parameter! Otherwise, the result link in the execution task overview will not show any test results.error

#### 2.5.4.2. How should I configure the Resource Adapter for the Execution with Jenkins?

The test bench needs to have **test.guide** **ResourceAdapter** started. If you use ecu.test to run the test bundles in your Jenkins job, no ecu.test execution may run there, otherwise the test bench will be considered busy and does not accept new tasks. The following **ResourceAdapter** plugins have to be configured:

- **Execution-Plugin**
- **Jenkins-Agent-Plugin**

Example configurations for each plugin can be found in **ResourceAdapter** example config.

### 2.5.5. Execution of generic tasks

#### 2.5.5.1. How does the task execution work for generic tasks?

The **ResourceAdapter** allows the execution of arbitrary commands on the test bench. Therefore, the generic dispatcher can be configured in the **ResourceAdapter** configuration.

The execution task that shall be executed on the test bench needs to have a playbook that only contains steps of type "command". Steps of this type contain a list of strings that represent the command to be executed. Furthermore, additional environment variables can be specified.

Example: the following command step will output the value of the additional environment variable `NEW_ENV` through a python script:

    {
      "type": "command",
      "command": [
        "python",
        "-c",
        "import os; print(os.environ['NEW_ENV'])"
      ],
      "environmentVariables": [
        {
          "label": "NEW_ENV",
          "value": "Hello World"
        }
      ]
    }

For more information on the command playbook step, see the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

If you want to create a report for your command step, you can create a report e.g. in JSON format. The path where the **ResourceAdapter** will search for a report is provided via the environment variable `TT_TASK_REPORT_DESTINATION`. If **ResourceAdapter** finds a report at the specified path, it will automatically upload the report to **test.guide** for you. See <u style="color: blue;">here</u> for more information about the available report formats.

The command to be executed will not be run in a command line tool like CMD, PowerShell or bash. You may execute your command inside a command line tool by specifying it in the command step, for example, if you want to run a batch script: `cmd /C .\Scripts\myScript.bat parameter`. Note, that you may have to address the batch script using backslashes on windows.info

#### 2.5.5.2. How should I configure the ResourceAdapter for the Execution of generic tasks?

The test bench needs to have **test.guide** **ResourceAdapter** started. The following **ResourceAdapter** plugins have to be configured:

- **Execution-Plugin**

In order to use the generic task execution the generic dispatcher has to be activated:

    plugin.de.tracetronic.ttstm.monitoring.plugin.execution.ExecutionPlugin.1.config.properties.dispatcher=generic

More information on the configuration of the Execution-Plugin can be found in the **ResourceAdapter** example config.

### 2.5.6. Playbooks

#### 2.5.6.1. What is a playbook?

A playbook describes a plan for a test execution. It references what shall be tested (the workspace and additional data), what shall be executed (setup steps, test cases and teardown steps) and where it shall be executed (XIL requirements).

For the actual execution you can create one or more execution tasks from a playbook. These tasks can then run independently on different test benches. This way you can parallelize your test executions.

Playbooks can only be executed directly **with ecu.test** or via the generic test execution and not with user defined Jenkins jobs. For the generic test execution only "command" playbook steps are allowed within the playbook.error

#### 2.5.6.2. How can I create a playbook?

Playbooks can be created via " **Upload playbook** " under **Playbooks**. There you can upload a **JSON file** (\*.json) to **test.guide** that describes the playbook. The file must at least contain the following information:

- `"metadata"` - metadata that describe the playbook
  - `"name"` - the name of the playbook
- `"workspace"` - all sources that are required to run the tests
  - `"source"` - the source of the ecu.test workspace, refer to <u style="color: blue;">source information of test bundles</u>
- `"execution"` - a container for the test cases
  - `"testcases"` - a list of the test cases that will be executed

An example playbook could look like this:

    {
        "metadata": {
            "name": "MyPlaybook"
        },
        "workspace": {
            "source": {
                "sourceType": "scm",
                "scmType": "git",
                "scmUrl": "https://my/repo.git",
                "scmCommit": "master",
                "relativeWorkspacePath": "path/to/workspace"
            },
            "dependencies": [
                {
                    "label": "A2L",
                    "source": {
                        "sourceType": "artifact",
                        "artifactId": "mydepot-123"
                    }
                }
            ]
        },
        "setup" : {
            "steps" : [
                {
                    "type" : "ecuTestStart"
                }
            ]
        },
        "execution": {
            "testcases": [
                {
                    "type": "command",
                    "command": ["python", "my_tests.py"]
                },
                {
                    "type": "project",
                    "relativePath": "Packages/MyProject.prj",
                    "constants": [
                        {
                            "label": "a2lPath",
                            "value": "'${A2L}'"
                        }
                    ],
                    "timeout": 10
                },
                {
                    "type": "package",
                    "relativePath": "Packages/MyPackage.pkg",
                    "packageParameters": [
                        {
                            "label": "startingSpeed",
                            "value": "42.0"
                        }
                    ]
                }
            ]
        },
        "teardown" : {
            "steps" : [
                {
                    "type" : "ecuTestStop"
                }
            ]
        },
        "xilConfigRequirements": [
            {
                "label": "Identifier",
                "category": "Type",
                "value": "FAS"
            }
        ]
    }

You can find a more detailed description of the playbook schema in the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

After uploading, each playbook gets a revision number. If you upload a playbook with a specific name for the first time, the playbook will get the revision number 1. If you upload a playbook with an already existing name, the playbook will get the next higher revision number. This way, different versions of a playbook can be tracked, and you can see the whole history of your playbook in **test.guide**.

You can also upload playbooks directly from **ecu.test** via the playbook export (see ecu.test documentation).info

Another possibility is to create playbooks via the **test.guide** user interface. Under **Playbooks** there is a button called **Add new playbook**. You then have to provide the workspace source of the newly created playbook. After submitting the workspace source, you will find yourself in the playbook editor, with an empty playbook.

#### 2.5.6.3. How can I prepare and clean up the environment for the test cases?

In addition to test cases (`"execution"` -section), playbooks can also contain a `"setup"` and a `"teardown"` section. Both contain steps for preparing or cleaning up the environment that is required for executing the test cases.

In the JSON description, the setup and teardown steps look quite similar to the test cases. A step type that exists only in the setup and teardown sections is the **configuration step**. This step contains relative paths to \*.tbc and \*.tcf files which should be loaded before the next package or project step. The keyword `"KEEP"` ensures that the previously loaded configuration is retained.

Starting and stopping **ecu.test** can be done explicitly by placing **ecu.test** start and stop steps anywhere in the setup or teardown section. If no start step is defined in setup or teardown, **ecu.test** will be startet by the **ResourceAdapter** right before the setup section begins. Accordingly, an **ecu.test** stop step will be automatically placed right after the teardown section if no such step has been defined explicitly. Therefore, it is possible to execute one or more command steps before starting or after shutting down **ecu.test**.

An example of using ecu.test start and stop steps could look like the following:

    "setup": {
        "steps": [
            {
                "command": [
                    "./scripts/someSetupScript.sh"
                ],
                "type": "command"
            },
            {
                "type": "ecuTestStart",
                "reuse": "never"
            }
        ]
    },
    "execution": {
        "testcases": [
            {
                "relativePath": "Packages/Testpackage.pkg",
                "type": "package"
            }
        ]
    },
    "teardown": {
        "steps": [
            {
                "type": "ecuTestStop"
            },
            {
                "command": [
                    "./scripts/someTeardownScript.sh"
                ],
                "type": "command"
            }
        ]
    }

You can also configure the **ecu.test** start steps to reuse a running **ecu.test** instance instead of restarting it. For this purpose the field `"reuse"` must be set to the value `"always"`. Also, **ecu.test** will not be closed at the end of the current execution, so that it can be reused for the following execution task (unless **ecu.test** stop steps are used). This way you can save the time for starting and stopping **ecu.test** over multiple playbook executions.

You can find a more detailed description of the playbook schema in the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API).

#### 2.5.6.4. How do I find my playbooks in test.guide?

You can find an overview of the latest revisions of all uploaded playbooks under **Playbooks**. Click on the details button next to a playbook to view the playbook details and switch to older revisions.

In both views you can also download the originally uploaded playbook via the "Download playbook" button. The prerequisite for this is that a playbook archive has been configured under **Settings**.

#### 2.5.6.5. How can I create execution tasks from a playbook?

After pressing the play button next to a playbook under **Playbooks**, a new window will open that shows some settings for creating execution tasks from the playbook. Here you can adjust the following information:

- the name and priority of the created execution tasks
- advanced settings for execution
  - the strategy of distributing the playbook to multiple execution tasks
    - If you chose "distribution by fixed number of partitions", you also need to specify how many tasks the playbook should be distributed to.
  - the execution mode of trace analyses attached to the test cases
  - user-defined parameters for the created execution tasks
  - Frequency of executions
    - As for <u style="color: blue;">execution tasks</u>, the execution of playbooks can be scheduled for delayed of recurring execution.
    - Equal to the execution of tasks, enabling `Check last execution` causes the recurring job to check if the last execution tasks created by this job are already terminated. Otherwise, no new execution tasks will be created.

The delayed or recurring execution will always execute the latest persisted version of the corresponding playbook. Thus, even if the execution has been created through the REST API providing a concrete playbook ID, a newer version of the playbook might be executed later on. Therefore, the option `Frequency of executions` will not be available if there are any unsaved changes in the playbook details page.info

All **user-defined parameters** of the execution task are available as constants in ecu.test- and as environment variables in command steps.info

After pressing the "Create" button, one or multiple execution tasks are created and queued according to their priority. Depending on the chosen distribution strategy, the created execution tasks have different contents:

- **No distribution**: Only one execution task is created. The source description, the test cases, the setup and teardown steps and the test resource requirements are taken over to the execution task.
- **Distribution by fixed number of partitions**: The source description, the setup and teardown steps and the test resource requirements are taken over to the execution tasks. The test cases will be distributed over the created execution tasks. This way you can parallelize your test executions.
- **Distribution on all currently matching test resources**: The source description, the test cases and the setup and teardown steps are taken over to the execution tasks. The currently matching test benches are determined. The test resource requirements are extended such that every matching test bench executes exactly one execution task. This way you can clone your test executions to all suitable test benches.

#### 2.5.6.6. Is it possible to have default parameters for the creation of execution tasks from playbooks?

In the playbook editor as well as via the **test.guide** REST-API it is possible to define playbook parameters. Playbook parameters have a name, which then corresponds to the name of the parameter in the created execution task. Furthermore, a default value can be set and parameters can be set as required. In addition, a description can be stored.

If a default value is provided by the playbook parameter you may override it by providing another value while <u style="color: blue;">creating the execution task from the playbook</u>. Parameters containing a default value can not be deleted and will always have at least their default value assigned to them after creating the execution task. If the parameter is set as required (while no default value is set), an execution task can only be created, if a parameter with this name is provided (see <u style="color: blue;">How to create execution tasks from playbooks</u> for more information).

#### 2.5.6.7. Can I change test resource requirements dynamically when creating execution tasks from a playbook?

It is possible to use variables of the form `${VAR}` in the `xilConfigRequirements` section of a playbook.

Example:

    "xilConfigRequirements": [{
        "category": "XIL",
        "label": "Identifier",
        "value": "${TEST-BENCH}"
    }]

When <u style="color: blue;">creating execution tasks from the playbook</u> you have to provide a value for each used variable as parameter of the playbook execution (a parameter named `TEST-BENCH` in the above example). In the resulting execution task, the variables will be replaced by the corresponding parameter values. The creation of the execution task will fail, if you use a variable without providing a corresponding parameter. However, you can escape a variable that should not be replaced by using the form `$${VAR}`. Variables may be used in every field of a test resource requirement and even in the details of the requirements.

For more information on test resource requirements, see <u style="color: blue;">here</u>.

#### 2.5.6.8. Which constants can be used in ecu.test during execution?

The test execution provides ecu.test with some special global constants that can be used during package or project execution. These are at least:

- **TT_TASK_ID**: the ID of the execution task
- all **user-defined parameters** of the execution task

If the execution task was created from a playbook, the following global constants are additionally provided:

- **TT_PLAYBOOK_ID**: the ID of the playbook
- **TT_PLAYBOOK_SECTION**: the playbook section where the playbook step belongs to with the value **SETUP**, **EXECUTION** or **TEARDOWN**
- **TT_PLAYBOOK_RUN_ID**: the ID of the playbook run
- **TT_PLAYBOOK_STEP_ID**: the ID of the playbook step to be executed

If the execution tasks source is an artifact from the **test.guide** artifact management, the following global constants are also provided:

- the ID of the artifact with the key **TT_ARTIFACT_ID**
- the download URL to the artifact with the key **TT_ARTIFACT_URL**

Additional global constants for package and project steps can be defined at the playbook step definition itself with the keyword `"constants"` (see the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API)).

This example shows how to use global constants in ecu.test: [Example.pkg](https://testguide.one-cx.cn/help-docs/020_Using/files/Example.pkg). For more information please see the ecu.test documentation.info

#### 2.5.6.9. Which environment variables can be used in script executions?

In a playbook you can use command steps for executing scripts (see <u style="color: blue;">generic dispatcher</u>) environment\>\>). The test execution provides the following environment variables in all script executions:

- **LOCATION**: location part of the resource location ID
- **TESTBENCH**: test bench part of the resource location ID
- **MACHINE**: machine part of the resource location ID
- **TEST_GUIDE_URL**: URL of the **test.guide** server defined in **ResourceAdapter** config
- **TEST_GUIDE_PROJECT_ID**: ID of the **test.guide** project defined in **ResourceAdapter** config
- **TEST_GUIDE_AUTH_KEY**: the authentication key of the **ResourceAdapter** for the access to **test.guide** defined in **ResourceAdapter** config
- **SOURCE_PATH**: absolute path to the source on the local machine
- **WORKSPACE_PATH**: absolute path to the workspace on the local machine (equals to the path to the source on the local machine concatenated with the relative workspace path specified in the task)
- **ECUTEST_EXECUTABLE**: absolute path to the ecu.test executable which is used for the test execution (if existing)
- all key-value pairs which are also provided as **global constants** in ecu.test (see <u style="color: blue;">Which constants can be used in ecu.test during execution?</u>)

Additional environment variables for command steps can be defined at the playbook step definition itself with the keyword `"environmentVariables"` (see the [Execution API Docs](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Execution%20API)).

Environment variables can be used in Batch-Files with `%VAR%` and in Shell-Files with `$VAR`.info

#### 2.5.6.10. Which environment variables can be used in ecu.test?

The test execution provides the following environment variables to be used in ecu.test packages, to execute user code easily:

- **LOCATION**: location part of the resource location ID
- **TESTBENCH**: test bench part of the resource location ID
- **MACHINE**: machine part of the resource location ID
- **TEST_GUIDE_URL**: URL of the **test.guide** server defined in **ResourceAdapter** config
- **TEST_GUIDE_PROJECT_ID**: ID of the **test.guide** project defined in **ResourceAdapter** config
- **ECUTEST_EXECUTABLE**: absolute path to the ecu.test executable which is used for the test execution (if existing)

In addition, all secret variables of the current test.guide project are delivered in the same way.

Environment variables can be used in ecu.test packages in Python functions and can be accessed with `os.environ["<name>"]`.info

#### 2.5.6.11. Which variables are automatically replaced in a playbook at the beginning of each execution?

You can use some special variables as placeholders in playbooks. At the beginning of an execution via the **ResourceAdapter**, these variables are automatically replaced by their resolved values.

The test execution provides and replaces the following variables:

- **LOCATION**: location part of the resource location ID
- **TESTBENCH**: test bench part of the resource location ID
- **MACHINE**: machine part of the resource location ID
- **TEST_GUIDE_URL**: URL of the **test.guide** server defined in **ResourceAdapter** config
- **TEST_GUIDE_PROJECT_ID**: ID of the **test.guide** project defined in **ResourceAdapter** config
- **TEST_GUIDE_AUTH_KEY**: authentication key of the **ResourceAdapter** for the access to **test.guide** defined in **ResourceAdapter** config
- all defined **workspace dependencies** labels (see <u style="color: blue;">workspace dependencies of execution tasks</u>)
- **SOURCE_PATH**: absolute path to the source on the local machine
- **WORKSPACE_PATH**: absolute path to the workspace on the local machine (equals to the path to the source on the local machine concatenated with the relative workspace path specified in the task)
- **ECUTEST_EXECUTABLE**: absolute path to the ecu.test executable which is used for the test execution (if existing)
- all defined **system environment variables**
- all labels becoming global constants (see <u style="color: blue;">Which constants can be used in ecu.test during execution?</u>)

All of these variables can be referenced with the notation `${VARIABLE_NAME}` in the following places of a playbook:

- in relative paths of testcases, setup steps and teardown steps
- in constant values of package or project steps
  - constant values have to be python expressions, if you want to use a string value additional quotation marks have to be set (e.g. `"'${VARIABLE_NAME}'"`)
  - special characters in expanded variables will be escaped
  - if you want to avoid escaping of the variables value you may prefix the variables name with "raw:" (e.g. `"${raw:VARIABLE_NAME}"`)
- in package parameter values of package steps
  - package parameter values have to be python expressions, if you want to use a string value additional quotation marks have to be set (e.g. `"'${VARIABLE_NAME}'"`)
  - special characters in expanded variables will be escaped
  - if you want to avoid escaping of the variables value you may prefix the variables name with "raw:" (e.g. `"${raw:VARIABLE_NAME}"`)
- in the relative workspace path of the workspace source
- in the "copy to"-path of workspace dependencies
- in the commit reference and sparse checkout path of SCM sources
- in the path of location sources
- in the URL of link sources
- in the artifact ID of artifact sources

Some variables are not available for substitution in specific parts of a playbook/task:

- the following variables are not available for substitution in the source- and dependency-blocks of a playbook/task:
  - **workspace dependencies** labels
  - the variables **TT_ARTIFACT_ID** and **TT_ARTIFACT_URL**
  - the variables **SOURCE_PATH** and **WORKSPACE_SOURCE**
- the variable **TT_PLAYBOOK_SECTION** can only be replaced in setup-, execution- und teardown-blocks of a playbook
- the variables **TT_PLAYBOOK_STEP_ID** and **TT_PLAYBOOK_STEP_ANALYSIS_ID** can only be replaced in the execution-block of a playbook
- the variables **TT_ARTIFACT_ID** and **TT_ARTIFACT_URL** can only be replaced if the workspace source is an artifact

Occurrences of `${…​}` in playbooks which are not supposed to be replaced have to be escaped with `$${…​}`.info

#### 2.5.6.12. What happens if the execution of a playbook step fails?

The following table describes which states a playbook step assumes for which test results. A general error in this context means that the step could not be executed, or the test report could not be created:

|  | Verdict SUCCESS, NONE or INCONCLUSIVE | Verdict FAILED or ERROR | General Error |
|----|----|----|----|
| **Setup step** | ✓ | ✗ | ✗ |
| **Test case** | ✓ | ✓ | ✗ |
| **Teardown step** | ✓ | ✓ | ✗ |

The state of the execution task results from the aggregated states of all playbook steps.

##### 2.5.6.12.1. Setup steps

The whole setup may fail for example in the following cases:

- a setup step is finished with verdict "ERROR" or "FAILED"
- the package or project associated with a setup step does not exist
- a setup step runs into a general error
- a setup step is cancelled manually

In all of these cases the execution of the setup is aborted immediately, the test cases are skipped and the execution of the teardown steps is started. The state of the execution task is set to **error**.

##### 2.5.6.12.2. Test cases

Test cases are completely independent of each other during the execution. This means if a test case fails with the verdict "FAILED" or "ERROR", the execution is not aborted, but the remaining test cases are executed normally. The state of the execution task will be set to **finished** at the end of the execution.

If a test case runs into a general error, the remaining test cases are executed normally and the state of the execution task is set to **error** at the end of the execution.

If you cancel the execution of a test case yourself, for example by manually aborting the test execution in ecu.test, the execution of the test cases will be stopped immediately, the execution of the teardown steps is started and the state of the execution task is set to **error** at the end of the execution.

##### 2.5.6.12.3. Teardown steps

If a teardown step fails with the verdict "FAILED" or "ERROR", the execution is not aborted, but the remaining teardown steps are executed normally. The state of the execution task will be set to **finished** at the end of the execution.

If you cancel the execution of a teardown step yourself, for example by manually aborting the test execution in ecu.test, or the teardown step runs into a general error the remaining teardown steps are executed normally and the state of the execution task is set to **error** at the end of the execution.

## 2.6. Using the workflow automation

## 2.6. 使用 workflow automation

### 2.6.1. Introduction

### 2.6.1. 简介

With the workflow automation, you can easily create the automation for your individual test processes within **test.guide**. Using simple blocks you can construct your user-defined workflows which are triggered by events in **test.guide**. Triggering events for the workflows can be

使用 workflow automation，您可以轻松为 **test.guide** 中的个人测试流程创建自动化。使用简单的块，您可以构建由 **test.guide** 中的事件触发的用户定义工作流。工作流的触发事件可以是：

- **test.guide** internal (e.g. a new artifact was uploaded to **test.guide** or a **test.guide** release was locked) or

- **test.guide** external (e.g. call triggered by a status change of a Jira ticket).

- **test.guide** 内部事件（例如，一个新的 artifact 被上传到 **test.guide** 或 **test.guide** release 被锁定）或

- **test.guide** 外部事件（例如，由 Jira ticket 状态更改触发的调用）。

Examplary use cases for the workflow automation:

workflow automation 的示例用例：

- Automatically start a test execution if a new software deliverable was uploaded to **test.guide**.

- Automatically change the status of a related Jira ticket if a release in **test.guide** was locked.

- 当新的软件可交付物被上传到 **test.guide** 时，自动启动测试执行。

- 当 **test.guide** 中的 release 被锁定时，自动更改相关 Jira ticket 的状态。

#### 2.6.1.1. How can you use the workflow automation?

#### 2.6.1.1. 如何使用 workflow automation？

The following image and description gives a high-level overview of the elements and steps involved in the workflow automation.

下面的图像和描述提供了 workflow automation 中涉及的元素和步骤的高级概述。
[Open: Pasted image 20260413221614.png](../attachments/images/c48ce0718da636d9fdbd3713470d06ae_MD5.png)
![c48ce0718da636d9fdbd3713470d06ae_MD5](test.guide%20user%20documentation-media/0a76ebfab5491e40fa298d03b79036193d274b77.png)

<table>

<colgroup>

<col>

<col>

<col>

</colgroup>

<tbody>

<tr>

<th rowspan="2">

<p>

Manual setup
</p>

</th>

<th>

<p>

1.  <a href="#using_workflow_automation_requirements">Flow bundle</a>
    </p>

    </th>

    <td>

    <p>

    A flow bundle is an artifact which automates your user-defined workflow. It consists of
    </p>

    ::: {}
    <ul>

    <li>

    <p>

    the flow definition (a runnable description of your workflow) and
    </p>

    </li>

    <li>

    <p>

    the flow.kit (a framework to create and execute a flow definition).
    </p>

    </li>

    </ul>
    :::

    <p>

    In the flow definition you represent your workflow by configuring and connecting flow blocks from the flow.kit library. Each flow block encapsulates an action to perform, e.g. requests to <strong>test.guide</strong> or external tools, a local operation.
    </p>

    </td>

    </tr>

    <tr>

    <th>

    <p>

    2.  <a href="#using_workflow_automation_trigger">Flow trigger</a>
        </p>

        </th>

        <td>

        <p>

        You create a flow trigger for your flow bundle. The flow trigger connects the flow bundle with a specification for <strong>test.guide</strong> events. This event specification defines the events on which your flow bundle reacts. These events can be <strong>test.guide</strong> internal (e.g. a new artifact was uploaded to <strong>test.guide</strong>) or external (e.g. call triggered by a status change of a Jira ticket).
        </p>

        </td>

        </tr>

        <tr>

        <th rowspan="3">

        <p>

        Automatic execution
        </p>

        </th>

        <th>

        <p>

        3.  <a href="#using_workflow_automation_task">Flow task</a>
            </p>

            </th>

            <td>

            <p>

            If an event occurs that matches a flow trigger's event specification, a flow task is created. The flow task contains the specific event information (e.g. id of the uploaded artifact) and a link to the flow bundle which is specified in the flow trigger.
            </p>

            </td>

            </tr>

            <tr>

            <th>

            <p>

            4.  <a href="#using_workflow_automation_execution_by_ra">Flow bundle execution</a>
                </p>

                </th>

                <td>

                <p>

                The flow task is fetched for execution by a <strong>ResourceAdapter</strong> with activated flow automation plugin. It runs your flow bundle providing it with the information of the specific event that triggered the flow task.
                </p>

                </td>

                </tr>

                <tr>

                <th>

                <p>

                5.  <a href="#using_workflow_automation_flow_report">Flow report</a>
                    </p>

                    </th>

                    <td>

                    <p>

                    After running your flow bundle, the Flow Automation plug-in creates a report for the flow task execution: a flow report. The flow report is uploaded to <strong>test.guide</strong> and shows detailed information about the execution of your flow bundle.
                    </p>

                    </td>

                    </tr>

                    </tbody>

                    </table>

<table>

<colgroup>

<col>

<col>

<col>

</colgroup>

<tbody>

<tr>

<th rowspan="2">

<p>

手动设置
</p>

</th>

<th>

<p>

1.  <u style="color: blue;">Flow bundle</u>
    </p>

    </th>

    <td>

    <p>

    flow bundle 是一个自动化您的用户定义工作流的 artifact。它由以下组成
    </p>

    ::: {}
    <ul>

    <li>

    <p>

    flow definition（您的工作流的可运行描述）和
    </p>

    </li>

    <li>

    <p>

    flow.kit（创建和执行 flow definition 的框架）。
    </p>

    </li>

    </ul>
    :::

    <p>

    在 flow definition 中，您通过配置和连接来自 flow.kit 库的 flow blocks 来表示您的工作流。每个 flow block 封装一个要执行的操作，例如对 <strong>test.guide</strong> 或外部工具的请求、本地操作。
    </p>

    </td>

    </tr>

    <tr>

    <th>

    <p>

    2.  <u style="color: blue;">Flow trigger</u>
        </p>

        </th>

        <td>

        <p>

        您为 flow bundle 创建一个 flow trigger。flow trigger 将 flow bundle 与 <strong>test.guide</strong> 事件的规范连接起来。此事件规范定义了您的 flow bundle 响应的事件。这些事件可以是 <strong>test.guide</strong> 内部事件（例如，一个新的 artifact 被上传到 <strong>test.guide</strong>）或外部事件（例如，由 Jira ticket 状态更改触发的调用）。
        </p>

        </td>

        </tr>

        <tr>

        <th rowspan="3">

        <p>

        自动执行
        </p>

        </th>

        <th>

        <p>

        3.  <u style="color: blue;">Flow task</u>
            </p>

            </th>

            <td>

            <p>

            如果发生与 flow trigger 的事件规范匹配的事件，则创建 flow task。flow task 包含特定事件信息（例如，已上传 artifact 的 id）以及对 flow trigger 中指定的 flow bundle 的链接。
            </p>

            </td>

            </tr>

            <tr>

            <th>

            <p>

            4.  <u style="color: blue;">Flow bundle 执行</u>
                </p>

                </th>

                <td>

                <p>

                flow task 由激活了 flow automation plugin 的 **ResourceAdapter** 获取以供执行。它运行您的 flow bundle，为其提供触发 flow task 的特定事件的信息。
                </p>

                </td>

                </tr>

                <tr>

                <th>

                <p>

                5.  <u style="color: blue;">Flow report</u>
                    </p>

                    </th>

                    <td>

                    <p>

                    运行 flow bundle 后，Flow Automation plug-in 为 flow task 执行创建报告：flow report。flow report 被上传到 <strong>test.guide</strong> 并显示有关 flow bundle 执行的详细信息。
                    </p>

                    </td>

                    </tr>

                    </tbody>

                    </table>

### 2.6.2. Requirements to setup workflow automation

### 2.6.2. 设置 workflow automation 的要求

The following initial steps are required to use the workflow automation:

使用 workflow automation 需要以下初始步骤：

- Flow bundle creation:
  - You need to create a flow bundle for your workflow using the flow.kit. The flow.kit is a framework to create flow bundles which automate your user-defined workflows.
- Flow bundle 创建：
  - 您需要使用 flow.kit 为您的工作流创建一个 flow bundle。flow.kit 是一个框架，用于创建自动化您的用户定义工作流的 flow bundles。

You can download a template flow bundle with the flow.kit from the Flow trigger overview page (see section <u style="color: blue;">Flow trigger</u>). You build your flow bundle by adapting this downloaded flow bundle.lightbulb_2

您可以从 Flow trigger 概览页面下载包含 flow.kit 的模板 flow bundle（请参阅 <u style="color: blue;">Flow trigger</u> 部分）。您通过调整这个下载的 flow bundle 来构建您的 flow bundle。lightbulb_2

A description on how to create your flow bundle is provided within the downloaded flow bundle.lightbulb_2

有关如何创建 flow bundle 的描述提供在下载的 flow bundle 中。lightbulb_2

- Flow source preparation:
  - To use a flow bundle for the workflow automation you need to make it available for test.guide. You have two options to make flow bundles available:
    - push the flow bundle to a **SCM (source code management)** and add a reference to the repository in test.guide (see *Project settings \> SCM tools* for details)
    - add a flow bundle as a zipped artifact to the **artifact management** (See *Artifact Management* for details)
- Flow source 准备：
  - 要使用 flow bundle 进行 workflow automation，您需要使其对 test.guide 可用。您有两个选项来使 flow bundles 可用：
    - 将 flow bundle 推送到 **SCM (source code management)**，并在 test.guide 中添加对存储库的引用（详细信息请参阅 *Project settings \> SCM tools*）
    - 将 flow bundle 作为压缩的 artifact 添加到 **artifact management**（详细信息请参阅 *Artifact Management*）
- **ResourceAdapter** configuration:
  - To have execution resources for the workflow automation you need to enable and configure the flow automation plugin in the **ResourceAdapter**.
  - See <u style="color: blue;">**ResourceAdapter** plug-in configuration</u> for how to configure the **ResourceAdapter**.
  - Refer to the `resourceAdapter.example.config` file for full information about the configuration options of the flow automation plugin.
- **ResourceAdapter** 配置：
  - 要为 workflow automation 拥有执行资源，您需要在 **ResourceAdapter** 中启用和配置 flow automation plugin。
  - 有关如何配置 **ResourceAdapter** 的信息，请参阅 <u style="color: blue;">**ResourceAdapter** plug-in configuration</u>。
  - 有关 flow automation plugin 的配置选项的完整信息，请参考 `resourceAdapter.example.config` 文件。

The `resourceAdapter.example.config` can be found in the extracted **ResourceAdapter** package.lightbulb_2

`resourceAdapter.example.config` 可以在提取的 **ResourceAdapter** 包中找到。lightbulb_2

- User permissions for **ResourceAdapter** user:
  - The \*\*\*\*test.guide\*\* user of the **ResourceAdapter**\*\* needs the project permission **Execute flow tasks**.
  - If the flow bundles are provided via the **artifact management**, the **test.guide** user of the **ResourceAdapter** also requires **Read/download** permission for the corresponding depositories.
- **ResourceAdapter** 用户的用户权限：
  - **ResourceAdapter** 的 **test.guide** 用户需要项目权限 **Execute flow tasks**。
  - 如果 flow bundles 是通过 **artifact management** 提供的，**ResourceAdapter** 的 **test.guide** 用户还需要对相应 depositories 的 **Read/download** 权限。

### 2.6.3. Flow trigger

### 2.6.3. Flow trigger

<figure>
<img
src="test.guide%20user%20documentation-media/030f4775ff394efdf16397dfe1619481c284ec97.png"
alt="203d8bef16d61fc470ffb7cf3ad4f3e7_MD5" />
<figcaption
aria-hidden="true">203d8bef16d61fc470ffb7cf3ad4f3e7_MD5</figcaption>
</figure>

WorkflowAutomationOverview Trigger

This chapter addresses the central part of the **test.guide** workflow automation: the flow trigger.

本章介绍了 **test.guide** workflow automation 的核心部分：flow trigger。

The flow trigger defines which **flow** bundle to execute for which **trigger** ing event. Flow triggers are defined per **test.guide** project.

flow trigger 定义了对哪个 **triggering** 事件执行哪个 **flow** bundle。Flow triggers 是按 **test.guide** 项目定义的。

The central entry point to configure flow triggers is the triggers page in **test.guide** (*Workflow automation \> Triggers*).

配置 flow triggers 的中央入口点是 **test.guide** 中的 triggers 页面（*Workflow automation \> Triggers*）。
[Open: Pasted image 20260413225605.png](../attachments/images/b236aab2ee2540bb81db005567a3beee_MD5.png)
![b236aab2ee2540bb81db005567a3beee_MD5](test.guide%20user%20documentation-media/b44fcc1c197397420f091ffee7a387788d4f19d6.png)

The page consists of 3 major elements:

该页面包含 3 个主要元素：

1.  Flow bundle download buttons

2.  Add flow trigger button

3.  Table of all configured flow triggers in this project

4.  Flow bundle 下载按钮

5.  添加 flow trigger 按钮

6.  此项目中所有已配置 flow triggers 的表格

#### 2.6.3.1. Creating a flow trigger

#### 2.6.3.1. 创建 flow trigger

The "Add flow trigger" button opens the following flow trigger dialog.

"Add flow trigger" 按钮打开以下 flow trigger 对话框。
[Open: Pasted image 20260413225707.png](../attachments/images/f7bc61eabe3e1a8a25cae3a9b2d743f6_MD5.png)
![f7bc61eabe3e1a8a25cae3a9b2d743f6_MD5](test.guide%20user%20documentation-media/bab3beb8a905f42db763d1a4ac832e3894a33483.png)

| Field | Description |
|----|----|
| Name | \- Your name for the flow trigger. The name should reflect the use case e.g. automatic test review.lightbulb_2 |
| Description | \- User description of the flow trigger. |
| Execution user | \- The execution user who executes the flow bundle. - This user needs all permissions relevant to the flow bundle and event. - The execution user has to be a technical user, which is authenticated by an authentication key. The option to use your own user is for test purposes only!bolt This is a security feature which ensures that you have access to the technical user at the point of time when changing the code that will be executed with these permissions. This security feature does apply to changes of the flow source and event type.lightbulb_2 |
| Source | \- The source of the flow bundle. - The flow bundle contains the implementation of your specific workflow automation. - Further information can be found in the section: <u style="color: blue;">Flow bundle source</u>. |
| Priority | \- Set on the tasks to determine execution order. - Available range 1 (least) to 100 (highest). |
| Threshold value of failed flow tasks for FAULTY flag | \- The number of consecutively failing flow tasks for the flow trigger to get flagged as FAULTY. If set to -1 the flow trigger will never get flagged as FAULTY. The FAULTY flag is set automatically by **test.guide** if the threshold is reached. This feature is to notify the user about problems of the flow trigger (e.g. 3rd party system unavailable) and prevent unnecessary execution tries. A **trigger flagged as FAULTY will still create flow tasks** to cover all incoming events. The created flow tasks will have the <u style="color: blue;">RETAINED</u> state.lightbulb_2 |
| Delete tasks older than (in days) | \- Time-based cleanup rule for tasks with a final state of this trigger. - The deciding factor for deletion is the task's completion time. - When left empty, tasks will not be removed automatically. |
| Event type | \- Event type on which this trigger subscribes. - Further information can be found in the section: <u style="color: blue;">Events and filters</u>. |
| Environment variables | \- Environment variables specific to the trigger to be passed to the flow bundle during execution. - Further information can be found in the section: <u style="color: blue;">Environment variables</u> |

| 字段 | 描述 |
|----|----|
| Name | \- 您为 flow trigger 的名称。名称应反映用例，例如自动测试审查。lightbulb_2 |
| Description | \- flow trigger 的用户描述。 |
| Execution user | \- 执行 flow bundle 的执行用户。- 此用户需要与 flow bundle 和事件相关的所有权限。- 执行用户必须是通过认证密钥认证的技术用户。使用您自己的用户选项仅供测试用途！bolt 这是一项安全功能，确保您在更改将使用这些权限执行的代码时有权访问技术用户。此安全功能适用于 flow source 和 event type 的更改。lightbulb_2 |
| Source | \- flow bundle 的来源。- flow bundle 包含您特定 workflow automation 的实现。- 更多信息可以在 <u style="color: blue;">Flow bundle source</u> 部分找到。 |
| Priority | \- 在任务上设置以确定执行顺序。- 可用范围 1（最低）到 100（最高）。 |
| Threshold value of failed flow tasks for FAULTY flag | \- 连续失败的 flow tasks 的数量，使 flow trigger 被标记为 FAULTY。如果设置为 -1，flow trigger 将永远不会被标记为 FAULTY。当达到阈值时，FAULTY 标志由 **test.guide** 自动设置。此功能用于通知用户 flow trigger 的问题（例如第三方系统不可用）并防止不必要的执行尝试。**标记为 FAULTY 的 trigger 仍然会创建 flow tasks** 来覆盖所有传入的事件。创建的 flow tasks 将具有 <u style="color: blue;">RETAINED</u> 状态。lightbulb_2 |
| Delete tasks older than (in days) | \- 对具有此 trigger 的最终状态的任务的基于时间的清理规则。- 删除的决定因素是任务的完成时间。- 当留空时，任务将不会自动删除。 |
| Event type | \- 此 trigger 订阅的事件类型。- 更多信息可以在 <u style="color: blue;">Events and filters</u> 部分找到。 |
| Environment variables | \- 特定于 trigger 的环境变量，在执行期间传递给 flow bundle。- 更多信息可以在 <u style="color: blue;">Environment variables</u> 部分找到。 |

When the trigger is created, it is active and will create flow tasks for matching events.

创建 trigger 后，它会激活并为匹配的事件创建 flow tasks。

#### 2.6.3.2. Events and filters

#### 2.6.3.2. 事件和过滤器

<figure>
<img
src="test.guide%20user%20documentation-media/051e46235071f470c743ec2270fc804832f3bc2a.png"
alt="df79a73e22ee567bea26a97092bc30b8_MD5" />
<figcaption
aria-hidden="true">df79a73e22ee567bea26a97092bc30b8_MD5</figcaption>
</figure>

WorkflowAutomationOverview Event

Some event types have additional filter options. The following table contains all event types and their corresponding filter options.

某些事件类型具有额外的过滤器选项。下表包含所有事件类型及其对应的过滤器选项。

Different filter items of an event are linked with a logical AND. Empty items are ignored.lightbulb_2

事件的不同过滤器项目与逻辑 AND 链接。空项目被忽略。lightbulb_2

| Event type | Description | Filter options |
|----|----|----|
| Appointment events<br/>[Appointment 事件]{style="background-color: #f0f0f0;"} | An appointment event occurred which means an appointment started or ended or it was created, updated or deleted.<br/>[Appointment 已开始、结束或被创建、更新、删除。]{style="background-color: #f0f0f0;"} | \- Type of appointment event<br/>- Appointment category<br/>- Test resource<br/>[- Appointment 事件类型<br/>- Appointment 分类<br/>- Test resource]{style="background-color: #f0f0f0;"} |
| Artifact uploads<br/>[Artifact 上传]{style="background-color: #f0f0f0;"} | An artifact is uploaded to a depository in the artifact management related to the project. The execution user needs access to the depository which the flow is designed for. No tasks are created for depositories to which the execution user does not have access.bolt<br/>[Artifact 上传到项目的 artifact 管理存储库。执行用户需要有存储库访问权限，若无权访问则不会创建任务。]{style="background-color: #f0f0f0;"} | \- Attributes<br/>    - artifact attributes as key-value filter<br/>    - values support wildcards<br/>- Depository ID<br/>- File name\*<br/>- File extension\*<br/>[- 属性<br/>    - artifact 属性作为键值过滤<br/>    - 值支持通配符<br/>- Depository ID<br/>- 文件名\*<br/>- 文件扩展名\*]{style="background-color: #f0f0f0;"} |
| Execution task state has changed<br/>[Execution task 状态变化]{style="background-color: #f0f0f0;"} | An execution task changes its state.<br/>[Execution task 的状态已改变。]{style="background-color: #f0f0f0;"} | \- Name\*<br/>- Attributes<br/>    - execution task attributes as key-value filter<br/>    - values support wildcards<br/>- New state<br/>[- 名称\*<br/>- 属性<br/>    - execution task 属性作为键值过滤<br/>    - 值支持通配符<br/>- 新状态]{style="background-color: #f0f0f0;"} |
| External event via REST API<br/>[REST API 外部事件]{style="background-color: #f0f0f0;"} | Event type to react on external events. This event type is designed to be used as webhook receiver addressed by other systems. Triggered by calling the API route: `<**test.guide** url>/api/triggers/<triggerId>/start`. For usage, refer to the Flow API doc. To start a flow task via the REST API an authentication key is needed. The user attached to the authentication key needs the **Flow task Create/Update** permission.lightbulb_2<br/>[用于响应外部事件，作为其他系统的 webhook 接收器。通过调用 `<**test.guide** url>/api/triggers/<triggerId>/start` 触发。需要 authentication key，关联用户需具有 **Flow task Create/Update** 权限。详见 Flow API 文档。lightbulb_2]{style="background-color: #f0f0f0;"} |  |
| PDF export<br/>[PDF 导出]{style="background-color: #f0f0f0;"} | An export of test result as PDF is finished.<br/>[测试结果的 PDF 导出已完成。]{style="background-color: #f0f0f0;"} | \- Report design\*<br/>- Report parameters<br/>    - Report parameters as key-value filter<br/>    - Values support wildcards<br/>[- Report design\*<br/>- Report parameters<br/>    - Report parameters 作为键值过滤<br/>    - 值支持通配符]{style="background-color: #f0f0f0;"} |
| Playbook run completed<br/>[Playbook 运行完成]{style="background-color: #f0f0f0;"} | A playbook run has been completed.<br/>[Playbook 已完成运行。]{style="background-color: #f0f0f0;"} | \- Playbook history ID<br/>- Playbook name\*<br/>[- Playbook history ID<br/>- Playbook 名称\*]{style="background-color: #f0f0f0;"} |
| Q-gate state has changed<br/>[Q-gate 状态变化]{style="background-color: #f0f0f0;"} | A Q-gate state has changed.<br/>[Q-gate 的状态已改变。]{style="background-color: #f0f0f0;"} | \- New Q-gate state<br/>- Q-gate plan key\*<br/>- Q-gate name\*<br/>[- 新 Q-gate 状态<br/>- Q-gate plan key\*<br/>- Q-gate 名称\*]{style="background-color: #f0f0f0;"} |
| Release state changes<br/>[Release 状态变化]{style="background-color: #f0f0f0;"} | A release state has changed.<br/>[Release 的状态已改变。]{style="background-color: #f0f0f0;"} | \- New release state<br/>- Release ID<br/>- Release type<br/>[- 新 release 状态<br/>- Release ID<br/>- Release 类型]{style="background-color: #f0f0f0;"} |
| Report uploads<br/>[Report 上传]{style="background-color: #f0f0f0;"} | A report got uploaded.<br/>[Report 已上传。]{style="background-color: #f0f0f0;"} | \- Project filter ID to filter uploaded test case executions<br/>[- Project filter ID 用于过滤已上传的 test case executions]{style="background-color: #f0f0f0;"} |
| Review creation<br/>[Review 创建]{style="background-color: #f0f0f0;"} | A review was created.<br/>[Review 已创建。]{style="background-color: #f0f0f0;"} | \- ID of a test case execution project filter to filter created reviews by the corresponding test case execution<br/>- Reevaluations to filter created reviews<br/>- Tags of the review to filter created reviews<br/>[- Test case execution project filter ID 以过滤相应的 reviews<br/>- Reevaluations 以过滤 reviews<br/>- Review 标签以过滤 reviews]{style="background-color: #f0f0f0;"} |
| Test case report export with flow trigger<br/>[Flow trigger 导出测试报告]{style="background-color: #f0f0f0;"} | The *Export report filter to flow trigger* button in the report filter GUI is clicked. It contains a list of selected test case execution IDs, which can be used to get more information. | \- Parameter Setup: Define parameters with unique names and with an optional default value directly in the trigger setup.<br/>- Execution Flexibility: When triggering you can either stick with your default values of parameters and trigger defined <u style="color: blue;">Environment variables</u> or manually override them for that specific run.<br/>[- 参数设置：在 trigger 设置中定义具有唯一名称和可选默认值的参数<br/>- 执行灵活性：运行时可使用默认参数值或手动覆盖 <u style="color: blue;">Environment variables</u>]{style="background-color: #f0f0f0;"} |
| Test resource machine went offline<br/>[Test resource 机器离线]{style="background-color: #f0f0f0;"} | Test resource machine sends no heartbeat.<br/>[Test resource 机器无法发送 heartbeat。]{style="background-color: #f0f0f0;"} |  |
| Time-controlled<br/>[时间控制]{style="background-color: #f0f0f0;"} | Event type for time-based triggering of flows.<br/>[基于时间的 flow trigger 事件类型。]{style="background-color: #f0f0f0;"} | \- Cron expression<br/>    - <https://man7.org/linux/man-pages/man5/crontab.5.html><br/>- Cron time zone<br/>    - Choose time zone base for Cron expression<br/>        - time zone of server<br/>        - local time zone<br/>[- Cron 表达式<br/>    - <https://man7.org/linux/man-pages/man5/crontab.5.html><br/>- Cron 时区<br/>    - 为 Cron 表达式选择时区<br/>        - server 时区<br/>        - local 时区]{style="background-color: #f0f0f0;"} |
| Workflow in a Q-gate plan<br/>[Q-gate plan 中的 workflow]{style="background-color: #f0f0f0;"} | Use this event type to specify a workflow that can be embedded in a Q-gate plan.<br/>[用此事件类型指定可嵌入 Q-gate plan 的 workflow。]{style="background-color: #f0f0f0;"} |  |

#### 2.6.3.3. Flow bundle source

#### 2.6.3.3. Flow bundle source

As the flow bundle source of a flow trigger you define the flow bundle which runs if a matching event occurs.

作为 flow trigger 的 flow bundle source，您定义了在匹配事件发生时运行的 flow bundle。

You have two options to provide your flow bundle as flow bundle source:

您有两个选项来提供您的 flow bundle 作为 flow bundle source：

- SCM source: a SCM (source code management) repository storing the flow bundle files

- Artifact source: an artifact in the **artifact management** storing the flow bundle

- SCM source：存储 flow bundle 文件的 SCM（source code management）存储库

- Artifact source：**artifact management** 中存储 flow bundle 的 artifact

##### 2.6.3.3.1. SCM (source code management)

##### 2.6.3.3.1. SCM (source code management)

The SCM source is configured on the flow trigger with the following dialog.

SCM source 在 flow trigger 上通过以下对话框配置。
[Open: Pasted image 20260413230220.png](../attachments/images/6314dce03f27d032fbe769bb2bad4625_MD5.png)
![6314dce03f27d032fbe769bb2bad4625_MD5](test.guide%20user%20documentation-media/f75046e8396038e055e92f47d10b230ff2cf9384.png)

| Field | Description |
|----|----|
| SCM label | Label of SCM that can be found in project settings. The SCM source uses the **test.guide** SCM configuration in the project settings. To use a an SCM repository as source, it first needs to be created there.lightbulb_2 |
| SCM commit | Commit reference in your SCM tool. Git specific commit hashes, branch names or tags can be used.lightbulb_2 |
| Sparse checkout path | (available for git) Sparse checkout selectively downloads parts of the repository. |
| Override SCM tool settings | Local override of settings made in the SCM configuration in the project settings. |
| Relative path | This relative path needs to point to your flow bundle, if the flow bundle is not at the root of the depository. When used in conjunction with sparse checkout, this path will be used relative to the checked out directory. For example: Sparse checkout path "folder" and relative path "subfolder" result in "folder/subfolder" in the application.lightbulb_2 |

| 字段 | 描述 |
|----|----|
| SCM label | 可在项目设置中找到的 SCM 的标签。SCM source 使用项目设置中的 **test.guide** SCM 配置。要将 SCM 存储库用作 source，首先需要在那里创建它。lightbulb_2 |
| SCM commit | SCM 工具中的提交引用。可以使用 Git 特定的提交哈希、分支名称或标签。lightbulb_2 |
| Sparse checkout path | （适用于 git）Sparse checkout 有选择性地下载存储库的部分。 |
| Override SCM tool settings | SCM 配置中在项目设置中进行的设置的本地覆盖。 |
| Relative path | 如果 flow bundle 不在 depository 的根目录，此相对路径需要指向您的 flow bundle。当与 sparse checkout 结合使用时，该路径将相对于检出的目录使用。例如：Sparse checkout 路径 "folder" 和相对路径 "subfolder" 在应用程序中导致 "folder/subfolder"。lightbulb_2 |

##### 2.6.3.3.2. Artifact

##### 2.6.3.3.2. Artifact

To use an artifact as flow source, the flow bundle needs to be uploaded to a depository in the **test.guide** **artifact management** as \*.zip file.

要将 artifact 用作 flow source，flow bundle 需要作为 \*.zip 文件上传到 **test.guide** **artifact management** 中的 depository。

The **ResourceAdapter** user need the **Read/download** permission on the depository in order to download the flow bundle during execution.bolt

**ResourceAdapter** 用户需要对 depository 的 **Read/download** 权限，以便在执行期间下载 flow bundle。bolt

Subsequently, you can configure an artifact source with this dialog:
[Open: Pasted image 20260414090424.png](../attachments/images/72266cc30aac892273c2768e4262b620_MD5.png)
![72266cc30aac892273c2768e4262b620_MD5](test.guide%20user%20documentation-media/f93ffea24683a08bfab45e2accc760216cbeb41f.png)

随后，您可以使用此对话框配置 artifact source：

| Field | Description |
|----|----|
| Artifact ID | ID of the artifact uploaded in the **artifact management**. |
| Relative Path | If the bundle is not in the root folder but a subfolder within the \*.zip archive, you need to set the relative path here. |

| 字段 | 描述 |
|----|----|
| Artifact ID | 在 **artifact management** 中上传的 artifact 的 ID。 |
| Relative Path | 如果 bundle 不在根文件夹中，而是在 \*.zip 存档中的子文件夹中，您需要在这里设置相对路径。 |

### 2.6.4. Flow task

### 2.6.4. Flow task

<figure>
<img
src="test.guide%20user%20documentation-media/8d93f6f671429889e087c6146f348477bbf00b01.png"
alt="6291c73b31143bba7e0f7212ba18ed97_MD5" />
<figcaption
aria-hidden="true">6291c73b31143bba7e0f7212ba18ed97_MD5</figcaption>
</figure>

WorkflowAutomationOverview Task

For every event matching the event specification of a flow trigger, a flow task is created.

对于与 flow trigger 的事件规范匹配的每个事件，都会创建一个 flow task。

You can access the overview page for all flow tasks under *Workflow Automation \> Tasks*. For every flow task, a detail page is available.

您可以在 *Workflow Automation \> Tasks* 下访问所有 flow tasks 的概览页面。对于每个 flow task，都有详细页面可用。

A flow task consists of:

一个 flow task 包括：

- a reference to the triggering flow trigger

- a flow source which is initially copied from the triggering flow trigger

- information of triggering event

- a <u style="color: blue;">flow block state</u>

- runtime meta information (ID of executing **ResourceAdapter**, start and end time of the execution)

- a flow report (detailed information for the flow task run)

- links related to the flow task run (trigger link and interaction links)

- links to the log files (if <u style="color: blue;">flow task log archive</u> was set)

- 对触发 flow trigger 的引用

- 最初从触发 flow trigger 复制的 flow source

- 触发事件的信息

- 一个 <u style="color: blue;">flow block state</u>

- 运行时元信息（执行 **ResourceAdapter** 的 ID、执行的开始和结束时间）

- flow report（flow task 运行的详细信息）

- 与 flow task 运行相关的链接（trigger 链接和交互链接）

- 日志文件的链接（如果设置了 <u style="color: blue;">flow task log archive</u>）

#### 2.6.4.1. Flow task states

#### 2.6.4.1. Flow task 状态

Every flow task has a state which shows its position in the flow task execution process.

每个 flow task 都有一个状态，显示其在 flow task 执行过程中的位置。

These are the states for a flow task as a whole. Flow blocks running as part of the flow task's flow definition have different states. These are described in the section <u style="color: blue;">flow block states</u>.lightbulb_2

这些是 flow task 整体的状态。作为 flow task 的 flow definition 的一部分运行的 flow blocks 具有不同的状态。这些在 <u style="color: blue;">flow block states</u> 部分中描述。lightbulb_2

The following flow task states exist:

以下 <mark style="background: #FF5582A6;">flow task 状态</mark>存在：

| Name | Description |
|----|----|
| WAITING | Flow task is ready to be executed by a **ResourceAdapter**. If a flow trigger goes into state FAULTY, all flow tasks which are in state WAITING and were created from that flow trigger go into state RETAINED. |
| RETAINED | Flow was not run and is retained from execution. It will not be fetched and run by a **ResourceAdapter** while it is in this state. A flow task can go into this state in two cases: - The flow task was triggered by a flow trigger that has a FAULTY flag. - The triggering flow trigger was flagged FAULTY while the flow task was in the state WAITING. If you fixed the reason for the fault, you can manually release the flow task. This brings this flow task in state WAITING. |
| RUNNING | Flow task is being executed by a **ResourceAdapter**. |
| FINISHED | Flow task was executed completely and without an error (all blocks of the flow definition have result <u style="color: blue;">FINISHED</u>). |
| SKIPPED | The flow task was executed without an error in a flow block but at least one block of the flow definition has result <u style="color: blue;">SKIPPED</u>. |
| ABORTED | An error occured while the flow task was executed. This can be - an error in the flow definition (the result of at least one block is <u style="color: blue;">ABORTED</u>). - an error outside the flow definition while trying to run it (e.g. error while fetching the flow (insufficient permissions, incorrect credentials for SCM repo)). |

| 名称 | 描述 |
|----|----|
| WAITING | Flow task 准备好由 **ResourceAdapter** 执行。如果 flow trigger 进入状态 FAULTY，所有处于 WAITING 状态且由该 flow trigger 创建的 flow tasks 进入 RETAINED 状态。 |
| RETAINED | Flow 未运行且从执行中保留。在此状态下，它不会被 **ResourceAdapter** 获取和运行。flow task 可以在两种情况下进入此状态：- flow task 由具有 FAULTY 标志的 flow trigger 触发。- 当 flow task 处于 WAITING 状态时，触发 flow trigger 被标记为 FAULTY。如果您修复了故障原因，您可以手动释放 flow task。这会将此 flow task 置于 WAITING 状态。 |
| RUNNING | Flow task 正由 **ResourceAdapter** 执行。 |
| FINISHED | Flow task 已完全执行且没有错误（flow definition 的所有块的结果都是 <u style="color: blue;">FINISHED</u>）。 |
| SKIPPED | flow task 在 flow block 中执行且没有错误，但 flow definition 的至少一个块的结果是 <u style="color: blue;">SKIPPED</u>。 |
| ABORTED | 执行 flow task 时发生错误。这可能是 - flow definition 中的错误（至少一个块的结果是 <u style="color: blue;">ABORTED</u>）。- 在尝试运行 flow 时 flow definition 外的错误（例如获取 flow 时出错（权限不足、SCM repo 凭证不正确））。 |

#### 2.6.4.2. Execution by the ResourceAdapter

#### 2.6.4.2. 由 ResourceAdapter 执行

<figure>
<img
src="test.guide%20user%20documentation-media/37cd716334492047c4d6f8692c31514a49199abc.png"
alt="3869763de14d853666f0abe938f7ce78_MD5" />
<figcaption
aria-hidden="true">3869763de14d853666f0abe938f7ce78_MD5</figcaption>
</figure>

WorkflowAutomationOverview Execution

The flow bundles of flow tasks are executed by **ResourceAdapter** s with configured Flow Automation plugin (see section <u style="color: blue;">Requirements</u> for details on the configuration). As the flow tasks run on systems with an active **ResourceAdapter**, all resources available on these machines can be accessed while running the flow bundle, e.g. present network drives.

flow tasks 的 flow bundles 由配置了 Flow Automation plugin 的 **ResourceAdapter** 执行（有关配置详细信息，请参阅 <u style="color: blue;">Requirements</u> 部分）。由于 flow tasks 在具有活动 **ResourceAdapter** 的系统上运行，运行 flow bundle 时可以访问这些机器上可用的所有资源，例如现有网络驱动器。

The available **ResourceAdapter** s fetch the flow tasks in state WAITING for execution. Currently, it is not possible to limit which flow tasks a **ResourceAdapter** can fetch and execute (e.g. no limitation based on operating system possible).lightbulb_2

可用的 **ResourceAdapter** 获取处于 WAITING 状态的 flow tasks 以供执行。目前，不可能限制 **ResourceAdapter** 可以获取和执行哪些 flow tasks（例如，没有基于操作系统的限制）。lightbulb_2

If both the execution task plugin and the flow automation plugin are enabled on the same **ResourceAdapter** runs of both plugins do not block each other.lightbulb_2

如果在同一 **ResourceAdapter** 上同时启用了execution task plugin和 flow automation plugin，两个 plugins 的运行不会相互阻塞。lightbulb_2

For every flow task execution the **ResourceAdapter** creates logs. These logs are located in the subdirectory `Flow_Automation_Resources\FlowKitLog` of the **ResourceAdapter** 's workspace directory with a separate directory for each flow task execution.

对于每个 flow task 执行，**ResourceAdapter** 创建日志。这些日志位于 **ResourceAdapter** 的工作区目录的 `Flow_Automation_Resources\FlowKitLog` 子目录中，每个 flow task 执行都有单独的目录。

If the <u style="color: blue;">depository for log file upload</u> is set execution log files are automatically uploaded to **test.guide** and can be accessed by links on the <u style="color: blue;">flow task detail page</u>.lightbulb_2

如果设置了 <u style="color: blue;">depository for log file upload</u>，执行日志文件会自动上传到 **test.guide**，可以通过 <u style="color: blue;">flow task detail page</u> 上的链接访问。lightbulb_2

Every flow task execution creates the following files:

每个 flow task 执行创建以下文件：

| File name | Description |
|----|----|
| payload.json | Payload of the flow task for the flow bundle execution |
| flowKitValidate.log | Validation phase log of the flow bundle execution Can be automatically uploaded to the **test.guide** <u style="color: blue;">depository for log file upload</u> |
| flowKitExecute.log | Execution phase log of the flow bundle execution Can be automatically uploaded to the **test.guide** <u style="color: blue;">depository for log file upload</u> |
| report.json | Report of the last flow bundle execution |

| 文件名 | 描述 |
|----|----|
| payload.json | flow bundle 执行的 flow task 的 Payload |
| flowKitValidate.log | flow bundle 执行的验证阶段日志。可以自动上传到 **test.guide** <u style="color: blue;">depository for log file upload</u> |
| flowKitExecute.log | flow bundle 执行的执行阶段日志。可以自动上传到 **test.guide** <u style="color: blue;">depository for log file upload</u> |
| report.json | 最后一次 flow bundle 执行的报告 |

#### 2.6.4.3. Flow report

#### 2.6.4.3. Flow report

<figure>
<img
src="test.guide%20user%20documentation-media/01e4abaeaaa873abfef70e7eef6636f3a0af0869.png"
alt="6bf72decf7036a16e42afce05d5d5aef_MD5" />
<figcaption
aria-hidden="true">6bf72decf7036a16e42afce05d5d5aef_MD5</figcaption>
</figure>

WorkflowAutomationOverview Report

The flow report for a flow task can be viewed on the detail page of the flow task. It is available after the execution of a flow task. The following screenshot shows an example for the flow report.

可以在 flow task 的详细页面上查看 flow task 的 flow report。它在 flow task 执行后可用。以下屏幕截图显示了 flow report 的示例。

The report shows information about the flow blocks of the flow definition for the flow bundle execution. The report includes a graphical visualisation of the run flow definition and the following information for every flow block:

报告显示有关 flow bundle 执行的 flow definition 的 flow blocks 的信息。报告包括运行 flow definition 的图形可视化以及每个 flow block 的以下信息：

- type of the flow block

- state of the flow block (see section <u style="color: blue;">flow block states</u>)

- dependencies (dependency flow blocks of this flow block)

- parameters (name and value of all parameters of this flow block)

- result

- errors from the execution of this flow block

- links to related resources (see section <u style="color: blue;">links and interactions</u>)

- flow block 的类型

- flow block 的状态（请参阅 <u style="color: blue;">flow block states</u> 部分）

- 依赖关系（此 flow block 的依赖 flow blocks）

- 参数（此 flow block 的所有参数的名称和值）

- 结果

- 此 flow block 执行的错误

- 相关资源的链接（请参阅 <u style="color: blue;">links and interactions</u> 部分）

#### 2.6.4.4. Flow block states

#### 2.6.4.4. Flow block 状态

Reported states of the flow blocks can be the following:

报告的 flow blocks 状态可以是以下几种：

| Name | Description |
|----|----|
| INIT | Flow block was not executed yet. Present if only the validation was run. |
| FINISHED | Flow block was executed successfully. |
| SKIPPED | A flow block can have this state in two cases: - Flow block was executed and explicitly set to SKIPPED (e.g. flow block ConditionalSkip). - A dependency block of this flow block is SKIPPED or ABORTED. |
| ABORTED | Flow block was executed and resulted in an error. This leads to the state <u style="color: blue;">ABORTED</u> of the overall flow task. |

| 名称 | 描述 |
|----|----|
| INIT | Flow block 尚未执行。如果仅运行验证，则显示。 |
| FINISHED | Flow block 已成功执行。 |
| SKIPPED | flow block 可以在两种情况下处于此状态：- Flow block 已执行且显式设置为 SKIPPED（例如 flow block ConditionalSkip）。- 此 flow block 的依赖块是 SKIPPED 或 ABORTED。 |
| ABORTED | Flow block 已执行并导致错误。这导致整体 flow task 的状态为 <u style="color: blue;">ABORTED</u>。 |

#### 2.6.4.5. Links and interactions

#### 2.6.4.5. 链接和交互

[Open: Pasted image 20260414095812.png](../attachments/images/e1342bbf9d799f10d1bf43877a381d3e_MD5.png)
![e1342bbf9d799f10d1bf43877a381d3e_MD5](test.guide%20user%20documentation-media/2a58b82c1a44a2fa62a49fb1d72456ceb0539355.png)
The flow task detail page shows a links section. It contains links to resources connected to the flow task. There are 4 categories of links:

flow task 详细页面显示一个链接部分。它包含连接到 flow task 的资源的链接。有 4 种链接类别：

<table>

<colgroup>

<col>

<col>

<col>

</colgroup>

<thead>

<tr>

<th colspan="2">

Category
</th>

<th>

Description
</th>

</tr>

</thead>

<tbody>

<tr>

<th colspan="2">

<p>

Trigger event
</p>

</th>

<td>

<p>

Link to the <strong>test.guide</strong> resource connected with the triggering event of this flow task.
</p>

</td>

</tr>

<tr>

<th rowspan="3">

<p>

Interaction
</p>

</th>

<th>

<p>

Created
</p>

</th>

<td>

<p>

Links to resources created during the flow task run.
</p>

</td>

</tr>

<tr>

<th>

<p>

Updated
</p>

</th>

<td>

<p>

Links to resources updated during the flow task run.
</p>

</td>

</tr>

<tr>

<th>

<p>

Related
</p>

</th>

<td>

<p>

Links to resources that were used during the flow run (e.g. if a <strong>test.guide</strong> release was read) or generic links added as interactions in the flow definition.
</p>

</td>

</tr>

</tbody>

</table>

<table>

<colgroup>

<col>

<col>

<col>

</colgroup>

<thead>

<tr>

<th colspan="2">

类别
</th>

<th>

描述
</th>

</tr>

</thead>

<tbody>

<tr>

<th colspan="2">

<p>

Trigger event
</p>

</th>

<td>

<p>

与此 flow task 的触发事件相关联的 <strong>test.guide</strong> 资源的链接。
</p>

</td>

</tr>

<tr>

<th rowspan="3">

<p>

Interaction
</p>

</th>

<th>

<p>

Created
</p>

</th>

<td>

<p>

在 flow task 运行期间创建的资源的链接。
</p>

</td>

</tr>

<tr>

<th>

<p>

Updated
</p>

</th>

<td>

<p>

在 flow task 运行期间更新的资源的链接。
</p>

</td>

</tr>

<tr>

<th>

<p>

Related
</p>

</th>

<td>

<p>

在 flow 运行期间使用的资源的链接（例如，如果读取了 <strong>test.guide</strong> release）或在 flow definition 中作为交互添加的通用链接。
</p>

</td>

</tr>

</tbody>

</table>

In the **Interaction** categories a link to a single resource is only shown once. If a resource would fall into multiple categories it is only shown in the highest category. The order of the categories is the following: **Created \> Updated \> Related**. If that resource was triggering the flow task it is also shown as the **Trigger event**.

在 **Interaction** 类别中，对单个资源的链接仅显示一次。如果资源会归入多个类别，则仅在最高类别中显示。类别的顺序如下：**Created \> Updated \> Related**。如果该资源触发了 flow task，它也会显示为 **Trigger event**。

Example: If a release was created and read during the flow task execution it is only shown in the category **Created** and not in **Related**. If a change to this release triggered the flow task the **Trigger event** category will show a link to the release as well.lightbulb_2

示例：如果在 flow task 执行期间创建并读取了 release，则仅在 **Created** 类别中显示，而不在 **Related** 中显示。如果对此 release 的更改触发了 flow task，**Trigger event** 类别也会显示对 release 的链接。lightbulb_2

#### 2.6.4.6. Actions

#### 2.6.4.6. 操作

For flow tasks, the following actions are available.

对于 flow tasks，以下操作可用。

##### 2.6.4.6.1. Rerun flow task

##### 2.6.4.6.1. 重新运行 flow task

This action creates a new flow task copying the flow trigger reference and the event information of the original flow task. Regardless of the original flow tasks state, the state of the newly created flow task is WAITING.

此操作创建一个新的 flow task，复制原始 flow task 的 flow trigger 引用和事件信息。无论原始 flow task 的状态如何，新创建的 flow task 的状态都是 WAITING。

You can choose, which flow source should be used for the new task. There are up to three options:

您可以选择对新任务使用哪个 flow source。最多有三个选项：

- the flow source of the original flow task at creation

  - If the flow source is an SCM source: this will use the commit-ish reference of the original flow task

- the flow source of the original flow task at execution

  - this option is only available if the flow task was executed before with an SCM source
  - it will use the exact commit hash of the executed flow task

- the flow source of the flow trigger

- 创建时原始 flow task 的 flow source

  - 如果 flow source 是 SCM source：这将使用原始 flow task 的 commit-ish 引用

- 执行时原始 flow task 的 flow source

  - 此选项仅在以前使用 SCM source 执行 flow task 时可用
  - 它将使用执行 flow task 的确切 commit 哈希

- flow trigger 的 flow source

On tasks with the source type `EXPORT_TESTCASES_WITH_FLOW_TRIGGER` with environment variables defined in the trigger, there is an additional option to override the environment variables for the rerun. If not overridden, the environment variable defaults defined in the flow trigger will be used.

对于源类型为 `EXPORT_TESTCASES_WITH_FLOW_TRIGGER` 且在 trigger 中定义了环境变量的任务，有一个额外的选项来覆盖重新运行的环境变量。如果未覆盖，将使用 flow trigger 中定义的环境变量默认值。

**示例：** 假如一个 flow trigger 中原本设置了：

    ENV_USER = "admin"
    ENV_TIMEOUT = "300s"

当你重新运行这个任务时，你可以：
- 覆盖这些变量：改成 `ENV_USER = "tester"` 和 `ENV_TIMEOUT = "600s"`
- 保持不变：继续使用原来的 `admin` 和 `300s`

The rerun flow task is fetched and run independently of the original flow task. This means that it does not necessarily run on the same **ResourceAdapter** as the original flow task.

重新运行的 flow task 独立于原始 flow task 进行获取和运行。这意味着它不一定在与原始 flow task 相同的 **ResourceAdapter** 上运行。

You can only rerun flow tasks where the triggering flow trigger exists and was not deleted.

您只能重新运行触发 flow trigger 存在且未被删除的 flow tasks。

You need the permission **Flow tasks Create/Update** for this action.

您需要 **Flow tasks Create/Update** 权限来执行此操作。

##### 2.6.4.6.2. Delete flow task

##### 2.6.4.6.2. 删除 flow task

This deletes the selected flow task.

这将删除选定的 flow task。

You need the permission **Flow tasks Delete** for this action.

您需要 **Flow tasks Delete** 权限来执行此操作。

##### 2.6.4.6.3. Release retained flow task

##### 2.6.4.6.3. 释放保留的 flow task

**(Only for tasks in state <u style="color: blue;">RETAINED</u>)**

**（仅适用于处于 <u style="color: blue;">RETAINED</u> 状态的任务）**

Flow tasks in state RETAINED can be released. This changes its state to WAITING, thus marking them as executable. In a context menu, you can choose the flow source for the released flow task from two options:

处于 RETAINED 状态的 flow tasks 可以被释放。这将其状态更改为 WAITING，从而将其标记为可执行。在上下文菜单中，您可以从两个选项中选择已释放 flow task 的 flow source：

- keep flow source of flow task

- use current flow source of the flow trigger

- 保持 flow task 的 flow source

- 使用 flow trigger 的当前 flow source

You need the permission **Flow tasks Create/Update** for this action.

您需要 **Flow tasks Create/Update** 权限来执行此操作。

### 2.6.5. Environment variables

### 2.6.5. 环境变量

Environment variables are key value pairs that are available to the flow during execution. They can be configured in two places:

环境变量是在执行期间对 flow 可用的键值对。它们可以在两个地方配置：

- on the project level for all flow bundle executions of a **test.guide** project.
  - configuration on the page *Workflow automation \> Env variables*.
- on each trigger specifically for the flow task created by this trigger.
  - configuration in the flow trigger dialog when creating or editing a flow trigger.
- 在项目级别，用于 **test.guide** 项目的所有 flow bundle 执行。
  - 在 *Workflow automation \> Env variables* 页面上配置。
- 在每个 trigger 上，特别是对于此 trigger 创建的 flow task。
  - 在创建或编辑 flow trigger 时在 flow trigger 对话框中配置。

**Environment variables** that are defined **on triggers will override** environment variables with the **same key defined in the project** for flow tasks created by these triggers.error

在 **triggers** 上定义的**环境变量**将覆盖在**项目中定义的相同 key 的环境变量**，对于这些 triggers 创建的 flow tasks。error

In the flow bundle, the value can be accessed via the flow.kit block `ReadEnvVar` or the standard Python function `os.getenv('MY_ENV_VAR')`.lightbulb_2

在 flow bundle 中，可以通过 flow.kit block `ReadEnvVar` 或标准 Python 函数 `os.getenv('MY_ENV_VAR')` 访问值。lightbulb_2

To protect the variable content the values cannot be displayed again in **test.guide**.lightbulb_2

为了保护变量内容，值无法再在 **test.guide** 中显示。lightbulb_2

### 2.6.6. Settings

### 2.6.6. 设置

#### 2.6.6.1. Flow task log archive configuration

#### 2.6.6.1. Flow task 日志存档配置

You can select a depository for log file upload, where <u style="color: blue;">log files from flow task executions</u> will be uploaded. If no depository is selected, the log files will not be uploaded.

您可以选择一个 depository 用于日志文件上传，其中将上传 <u style="color: blue;">flow task 执行的日志文件</u>。如果未选择 depository，日志文件将不会上传。

The **ResourceAdapter** user needs the **Upload** permission on the depository to upload the log files.bolt

**ResourceAdapter** 用户需要对 depository 的 **Upload** 权限来上传日志文件。bolt

The uploaded log files for each flow task are linked on the <u style="color: blue;">flow task detail page</u>.

每个 flow task 的已上传日志文件都链接在 <u style="color: blue;">flow task detail page</u> 上。

You can setup remove rules in the depository settings to automatically remove old log files. For fine-grained control you can use the attributes `TT_FlowTaskId` (for selecting flow task execution log files in general) or `TT_FlowTriggerId` (for selecting log files of a specific flow trigger).lightbulb_2

您可以在 depository 设置中设置删除规则以自动删除旧日志文件。为了进行细粒度控制，您可以使用属性 `TT_FlowTaskId`（用于一般选择 flow task 执行日志文件）或 `TT_FlowTriggerId`（用于选择特定 flow trigger 的日志文件）。lightbulb_2

## 3 Integrating

This chapter provides information about tools that can interact with **test.guide**. If it is necessary to change the configuration of the external tool to allow interaction, these changes are explained in this chapter. If the configuration has to be done in **test.guide** have a look on <u style="color: blue;">menu:Project settings</u>.

## 3.1. Integrating in ecu.test

**ecu.test** and **test.guide** are well connected. To address your **test.guide** project within **ecu.test** just set up a few options in **ecu.test**. A short guide is directly accessible in **test.guide** at <u style="color: blue;">\*Configure report upload in ecu.test</u>.

## 3.2. Integrating in Jenkins

**tracetronic** provides an **ecu.test** plugin for Jenkins. Within this plugin **test.guide** can also be configured, see the [plugin documentation at GitHub](https://github.com/jenkinsci/ecutest-plugin).

## 3.3. Integrating in test.guide

The following sections act only as a short briefing about the possibilities of **test.guide**. For the configuration of the tools, see <u style="color: blue;">menu:Project settings</u>. For the usage of the features supported with the tools, see <u style="color: blue;">**Using**</u>.

### 3.3.1. Integrating issue trackers

Issue trackers can be utilized in **test.guide** to access your issue/defect management. You can create reviews or request the status of the linked tickets.

**test.guide** provides access to:

#### 3.3.1.1. Jira

When utilizing Jira, **test.guide** supports different authentication methods:

- HTTP basic authentication using username and password,
- HTTP basic authentication using username and an [API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) and
- HTTP bearer authentication by [Personal Access Token](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

When configuring the Jira connection, please select `Authentication Method: Basic Authentication` if one of the first two methods should be used. In case you want to make use of a Personal Access Token previously created in Jira, set `Authentication Method` to `Personal Access Token`.

When using a Personal Access Tokens, for technical reasons, **test.guide** will insist on a username to be entered. You can enter any value in the username field, it will not be used.info

### 3.3.2. Integrating test management tools

Test management tools (or Application Lifecycle Management (ALM) tools) can be used to synchronize test specification, test planning, all-in-all test management with the test report data of **test.guide**. Furthermore, it is possible to get access to your test plans and use them as data basis for coverages.

**test.guide** provides access to:

The connection of one of the tools can be configured over <u style="color: blue;">**Management tools**</u>.info

#### 3.3.2.1. Jama

If you want to use the test run \<\> defect linking of test.guide you have to provide the identification number for the relation type that you want to use. The easiest way to get this number is by using the Swagger UI of your Jama instance at <jama-url>/api-docs. Try out GET relationship types and choose the ID of your need.

### 3.3.3. Integrating source control management

**test.guide** allows integration of source control management (SCM) tools. These can be used to manage your test bundles for distributed test execution.

**test.guide** provides access to:

- Git-based SCM tools, e.g.:

### 3.3.4. Integrating metrics tools

**test.guide** provides three metrics endpoints for scraping with [Prometheus](https://www.prometheus.io/): \* [/api/metrics](https://testguide.one-cx.cn/api/metrics) provides operational metrics, for example JVM status, but also usage statistics \* [/api/metrics/performance](https://testguide.one-cx.cn/api/metrics/performance) provides performance-related metrics that provide an insight into the number of times performance-critical operations are executed and their average execution time \* [/api/metrics/database](https://testguide.one-cx.cn/api/metrics/database) provides metrics pertaining the database state and configuration

To get started a basic [Grafana](https://www.grafana.com/) dashboard can be used: [testguide_Dashboard.json](https://testguide.one-cx.cn/help-docs/030_Integrating/files/metrics/testguide_Dashboard.json)

This section is for intended for usage by *project managers*. The project settings made here affect all members of the project.

## 4.1. File repository

→ <u style="color: blue;">**File repository**</u>

For binary report data such as recordings, logs or plots to be available in the **test.guide**, a file repository must be configured in the project.

If the same file repository is to be used by several projects at the same time, it is essential to **ensure that each of the projects has its own subdirectory or unique key on the file repository** so that file collisions are not possible!bolt

There are a variety of storage types available that can be integrated via Depository from the **test.guide** artifact management. See <u style="color: blue;">How do I set up a depository?</u> for more information.

To be able to configure a file repository via a depository from the **test.guide** artifact management, your user account must have the *Read / Download* project role permission for the depository (see <u style="color: blue;">Configure project role permissions for the depository</u>).bolt

Separate remove rules and quotas are available via artifact management. However, to avoid data inconsistencies, only the remove rules/quotas for file repository should be used!warning

The following *settings are deprecated* but can still be edited:

- File system (may also be used with mounted network drives)
- FTP server
- [Artifactory Repository Manager](https://www.jfrog.com/artifactory/)
- Amazon S3 (Simple Storage Service)
- Server Message Block (SMB) / Common Internet File System (CIFS)

Assuming one can access the SMB resource by navigating to `\\my-storage-server\my-share\path\in\share` in Windows Explorer, this corresponds to the following SMB configuration in **test.guide**:

<figure>
<img
src="test.guide%20user%20documentation-media/9b35f13e97749c77822d45cd071f90424a2ac37a.png"
alt="c17f53e48372f22fde54d27b300a9a82_MD5" />
<figcaption
aria-hidden="true">c17f53e48372f22fde54d27b300a9a82_MD5</figcaption>
</figure>

SmbFileRepositoryExample

info

### 4.1.1. Migration

If a file repository moves from one storage (e.g. [NAS storage](https://de.wikipedia.org/wiki/Network_Attached_Storage)) to another storage and as a result, the access path changes, **test.guide** provides the option to migrate existing deposited files.

There is no downtime for new project uploads during the migration.info

### 4.1.2. File remove rules

Sometimes files need to be retained for a limited time period only, for example to analyze them. In this case, the *File remove rules* can be used to set which files are automatically removed from **test.guide** based on predefined criteria.

Using this feature may save a lot of storage space!lightbulb_2

## 4.2. Project users

→ <u style="color: blue;">**Project users**</u>

Each project manages its own users.

### 4.2.1. Let users register themselves instead of creating them beforehand

Users who want to join the project should not be created manually by the project manager, even though this is possible. Instead, they should register themselves at [/register](https://testguide.one-cx.cn/register).

### 4.2.2. Manage users in project context

At **Project users** menu, a project manager can maintain users, which are assigned to the project.

The following operations are available:

| Action | Description |
|----|----|
| Add new user | Create a new user, which is added to the project. This will send a notification if <u style="color: blue;">**Email**</u> is set up. |
| Add user to project | Add an existing user to the project. |
| Add technical user | Create a technical user account for this project. Technical users can only interact with test.guide using the API (upload reports, etc.). To learn how to get the authentication key of a technical user, please refer to <u style="color: blue;">"How can I upload my ecu.test reports to test.guide?"</u>. |
| Edit | Change the user's profile or project permissions. |
| Remove from project | Remove the user from this project, revoking former access privileges. |
| Deactivate | Disables access to the project, keeping project permissions untouched. The user can be reactivated later. |

### 4.2.3. Project permissions

Permissions can be granted user specific by clicking the **Edit** button next to the respective user. There are different context specific permissions that are described in the table below.

<table>

<colgroup>

<col>

<col>

<col>

<col>

<col>

</colgroup>

<thead>

<tr>

<th>

Context
</th>

<th>

Permission
</th>

<th colspan="2">

Description
</th>

<th>

API value
</th>

</tr>

</thead>

<tbody>

<tr>

<td>

<p>

General
</p>

</td>

<td>

<p>

Project management
</p>

</td>

<td colspan="2">

<p>

Allows the user to manage project settings such as
</p>

::: {}
<ul>

<li>

<p>

Config file storage, external tools
</p>

</li>

<li>

<p>

Config upload rules
</p>

</li>

<li>

<p>

Config filter settings, review settings
</p>

</li>

<li>

<p>

Export/import reports
</p>

</li>

<li>

<p>

Show project tasks in task manager
</p>

</li>

<li>

<p>

Send message to all users
</p>

</li>

<li>

<p>

Delete public report filter for other users
</p>

</li>

<li>

<p>

Delete public coverage filter for other users
</p>

</li>

<li>

<p>

Create and edit project filters
</p>

</li>

<li>

<p>

Create dashboards
</p>

</li>

</ul>
:::

</td>

<td>

<p>

PROJECT_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td>

<p>

General
</p>

</td>

<td>

<p>

Manage project users
</p>

</td>

<td colspan="2">

<p>

Allows the user to
</p>

::: {}
<ul>

<li>

<p>

create new users
</p>

</li>

<li>

<p>

add/remove existing users to/from project
</p>

</li>

<li>

<p>

edit project roles
</p>

</li>

<li>

<p>

edit and deactivate existing users
</p>

</li>

</ul>
:::

</td>

<td>

<p>

PROJECT_USER_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td>

<p>

Test report management
</p>

</td>

<td>

<p>

Manage business report templates
</p>

</td>

<td colspan="2">

<p>

Allows the user to access <a href="#nav_prj_reporting"><b>Reporting</b></a>
</p>

</td>

<td>

<p>

BUSINESSREPORT_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td>

<p>

Release management
</p>

</td>

<td>

<p>

Lock release
</p>

</td>

<td colspan="2">

<p>

Allows the user to lock releases in <b>Release overview</b>
</p>

</td>

<td>

<p>

LOCK_RELEASE
</p>

</td>

</tr>

<tr>

<td>

<p>

Release management
</p>

</td>

<td>

<p>

Unlock release
</p>

</td>

<td colspan="2">

<p>

Allows the user to unlock releases <b>Release overview</b>
</p>

</td>

<td>

<p>

UNLOCK_RELEASE
</p>

</td>

</tr>

<tr>

<td>

<p>

Test report management
</p>

</td>

<td>

<p>

Manage dashboards
</p>

</td>

<td colspan="2">

<p>

Allows the user to access <a href="#nav_prj_dashboardViews"><b>Dashboard views</b></a>
</p>

</td>

<td>

<p>

DASHBOARD_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td>

<p>

Test execution
</p>

</td>

<td>

<p>

Manage SCM configurations
</p>

</td>

<td colspan="2">

<p>

Allows the user to configure Source Control Management tools
</p>

</td>

<td>

<p>

SCM_CONFIG_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td>

<p>

Test report management
</p>

</td>

<td>

<p>

Manage project filters
</p>

</td>

<td colspan="2">

<p>

Allows the user to manage project filters at <a href="#nav_prj_projectFilters"><b>Project filters</b></a> and create new ones using the <b>Report filter</b>
</p>

</td>

<td>

<p>

PROJECT_FILTER_MANAGEMENT
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Test report management
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Test reports
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see test reports
</p>

</td>

<td>

<p>

TESTCASE_VIEWER
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to upload test reports to <strong>test.guide</strong>
</p>

</td>

<td>

<p>

TESTCASE_UPLOADER
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete test reports
</p>

</td>

<td>

<p>

UPLOAD_CLEANER
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Test report management
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Deposited files
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

To see deposited files of test reports, the user needs the "Read" permission for test reports
</p>

</td>

<td>

<p>

TESTCASE_VIEWER
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to attach files to test reports
</p>

</td>

<td>

<p>

ARCHIVE_UPLOADER
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete deposited files of test reports
</p>

</td>

<td>

<p>

ARCHIVE_DELETE
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Test report management
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Reviews
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

To see reviews of test reports, the user needs the "Read" permission for test reports
</p>

</td>

<td>

<p>

TESTCASE_VIEWER
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to create reviews for test reports
</p>

</td>

<td>

<p>

REVIEWER
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Deleting reviews is not possible
</p>

</td>

<td>

<p>

\-
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Release management
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Releases
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see releases
</p>

</td>

<td>

<p>

RELEASE_READ
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to create new or edit existing releases
</p>

</td>

<td>

<p>

RELEASE_CREATE
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete releases
</p>

</td>

<td>

<p>

RELEASE_DELETE
</p>

</td>

</tr>

<tr>

<td>

<p>

Monitoring (test infrastructure)
</p>

</td>

<td>

<p>

Monitoring management
</p>

</td>

<td colspan="2">

<p>

Allows the user to manage test resources and test resource machines (create, delete) and related features (activity types, attributes, appointment categories, ...) and enables access to <b>ResourceAdapters</b>, where the configurations of all <strong>ResourceAdapter</strong> s can be managed
</p>

</td>

<td>

<p>

HIL_ADMIN
</p>

</td>

</tr>

<tr>

<td>

<p>

Monitoring (test infrastructure)
</p>

</td>

<td>

<p>

Synchronize ResourceAdapter configuration
</p>

</td>

<td colspan="2">

<p>

Enables access to APIs required by <strong>ResourceAdapter</strong> s to synchronize their respective configuration files with the <strong>test.guide</strong> server
</p>

</td>

<td>

<p>

RA_CONFIG_SYNC
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Monitoring (test infrastructure)
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Monitoring data
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see test resource and test resource machine data within the modules "Test infrastructure" and the "Monitoring"
</p>

</td>

<td>

<p>

HIL_USER
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to add data of test resources and to upload test resource machine data to <strong>test.guide</strong> (e.g. used for technical users of <strong>ResourceAdapter</strong> s)
</p>

</td>

<td>

<p>

MONITORING_UPLOADER
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete data of test resources and test resource machines from the monitoring database of <strong>test.guide</strong>
</p>

</td>

<td>

<p>

MONITORING_DELETE
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Test execution
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Test executions
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see test execution tasks and playbooks within the Test execution module
</p>

</td>

<td>

<p>

EXECUTION_READ
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to
</p>

::: {}
<ul>

<li>

<p>

upload new test execution tasks and playbooks
</p>

</li>

<li>

<p>

add new playbooks
</p>

</li>

<li>

<p>

edit existing test execution tasks and playbooks
</p>

</li>

<li>

<p>

execute playbooks
</p>

</li>

<li>

<p>

rerun test execution tasks
</p>

</li>

</ul>
:::

</td>

<td>

<p>

EXECUTION_CREATE
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete execution tasks and playbooks
</p>

</td>

<td>

<p>

EXECUTION_DELETE
</p>

</td>

</tr>

<tr>

<td>

<p>

Workflow automation (<strong>ResourceAdapter</strong> flow automation plugin)
</p>

</td>

<td>

<p>

Execute flow tasks
</p>

</td>

<td colspan="2">

<p>

Permission to access APIs required to execute flow tasks, necessary for user of <strong>ResourceAdapter</strong> when using flow automation plugin
</p>

</td>

<td>

<p>

FLOW_TASK_EXECUTE
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Workflow automation
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Flow trigger
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see flow triggers within the workflow automation module.
</p>

</td>

<td>

<p>

FLOW_TRIGGER_READ
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to
</p>

::: {}
<ul>

<li>

<p>

add new flow triggers
</p>

</li>

<li>

<p>

edit existing flow triggers
</p>

</li>

<li>

<p>

activate/deactivate flow triggers
</p>

</li>

<li>

<p>

remove faulty flag on flow triggers
</p>

</li>

<li>

<p>

see flow secret entries
</p>

</li>

<li>

<p>

add new flow secrets
</p>

</li>

<li>

<p>

edit flow secrets.
</p>

</li>

</ul>
:::

</td>

<td>

<p>

FLOW_TRIGGER_CREATE
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete flow triggers and flow secrets.
</p>

</td>

<td>

<p>

FLOW_TRIGGER_DELETE
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Workflow automation
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Flow task
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see flow tasks within the workflow automation module
</p>

</td>

<td>

<p>

FLOW_TASK_READ
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to
</p>

::: {}
<ul>

<li>

<p>

rerun flow tasks
</p>

</li>

<li>

<p>

release flow tasks in state RETAINED.
</p>

</li>

</ul>
:::

</td>

<td>

<p>

FLOW_TASK_CREATE
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete flow tasks.
</p>

</td>

<td>

<p>

FLOW_TASK_DELETE
</p>

</td>

</tr>

<tr>

<td rowspan="3">

<p>

Release management
</p>

</td>

<td rowspan="3">

<p>

<strong>Category</strong> Q-gate plans
</p>

</td>

<td>

<p>

Read
</p>

</td>

<td>

<p>

Allows the user to see Q-gate plans and their details
</p>

</td>

<td>

<p>

QGATE_PLAN_READ
</p>

</td>

</tr>

<tr>

<td>

<p>

Create/Update
</p>

</td>

<td>

<p>

Allows the user to create Q-gate plans and manage a Q-gate plans properties (e.g. attributes) and contents (creating, editing and removing Q-gates and dependencies in between)
</p>

</td>

<td>

<p>

QGATE_PLAN_CREATE
</p>

</td>

</tr>

<tr>

<td>

<p>

Delete
</p>

</td>

<td>

<p>

Allows the user to delete Q-gate plans.
</p>

</td>

<td>

<p>

QGATE_PLAN_DELETE
</p>

</td>

</tr>

</tbody>

</table>

### 4.2.4. Project roles

Instead of assigning individual project permissions to users, you should use roles in your project and assign them to users.

<figure>
<img
src="test.guide%20user%20documentation-media/837195aae04211de552e72a8ad87fca1fd1e5d45.png"
alt="fbc966a40ef2fcad71d0587e5aa0edf8_MD5" />
<figcaption
aria-hidden="true">fbc966a40ef2fcad71d0587e5aa0edf8_MD5</figcaption>
</figure>

Figure 1. Relation between users, system groups and project roles

At **Project roles**, existing roles can be maintained and new roles created. The following operations are available:

| Action | Description |
|----|----|
| Edit | Change the permissions assigned to the role |
| Manage members | Assign and remove users, who are member of this role. The members inherit all permissions assign to the role. |
| Associate system groups | Besides individual users, system groups can be associated with a role. All users who are members of the associated system group will inherit membership of the role and therefore all permissions linked to it. See also <u style="color: blue;">System groups</u>. |
| Delete | Remove the role. The members will lose all permissions brought by this role. |

The roles assigned to a project user are also visible on the project user page where users can be assigned roles, too.

#### 4.2.4.1. Effective permissions

When working with project roles, individual permissions and system groups, it can be hard to find out which permissions a certain user has in the end. Therefore, when editing a project user and their permissions, you can see their roles and groups. Additionally you can use the "Show effective permissions"-button at the end of the form to get an overview of all their accumulated permissions.

### 4.2.5. Using project roles and system groups

- If you are using LDAP authentication and your LDAP directory contains groups that you want to use for authorization:
  1.  Enable the system group synchronization feature (see <u style="color: blue;">System groups</u>)
  2.  Create project roles
  3.  For each role, specify the permissions that the role members should have
  4.  Assign system groups with their project role counterparts
- If your authentication provider does not contain usable groups but you still want to use roles for permission management:
  1.  Create project roles
  2.  For each role, specify the permissions that the role members should have
  3.  Add users directly to the roles
- By best practices, individual permissions should rarely be used. Individual permission make it hard to keep track of which user has which permission and why.

## 4.3. Filter settings

→ <u style="color: blue;">**Filter settings**</u>

The report filter fields can be customized, for example to resemble the projects individual naming conventions. This will help project members to orientate.

New filter fields can also be defined for each project. More information can be found at <u style="color: blue;">**Customizing the report filter**</u>.

## 4.4. Review settings

→ <u style="color: blue;">**Review settings**</u>

To ensure that the review process is consistent, specific review requirements can be set in the project.

Besides the definition of

- defect classes
- defect priorities
- tags
- and custom evaluations

also the mandatory review fields can be set.

### 4.4.1. Link issues

Another review option operates in conjunction with a configured <u style="color: blue;">issue tracker</u> and releases. It automates linking between issues within the issue tracker. Currently supported system:

- Atlassian Jira (supports interlinking projects)

Even issues from different projects will be linkable. Any issues assigned to a release will be linked with issues assigned to reviews of test case executions added to the release. The link will be created on two occasions (assuming the release and reviews have issues assigned):

- Create a review on a test case execution that is part of a release (via browser or API)
- Add test case executions with existing reviews to a release (via browser or API)

To create a link between two issues the user credentials may be required, depending on the provided issue tracker configuration. When using the web frontend a prompt will be displayed. Requests on the API that encounter missing credentials will be aborted with http status 412 (precondition failed).info

## 4.5. Reporting

→ <u style="color: blue;">**Reporting**</u>

If you want to change content and design of test summary or test case coverage PDF reports, templates for PDF generation can be managed in this section.

Please refer to <u style="color: blue;">**Customizing the PDF export**</u> for more information on this topic.

## 4.6. Issue tracker

→ <u style="color: blue;">**Issue Tracker**</u>

**test.guide** supports the connection to various issue trackers. This way, defects detected during the review process can be directly fed back into the corresponding issue tracker. Due to the seamless integration, the user does not have to leave **test.guide** to do so.

More information about supported issue trackers and their configuration can be found at <u style="color: blue;">**Integrating issue trackers**</u>.

### 4.6.1. Issue tracker templates

To ease the process of creating defect tickets, individual templates can be defined for each issue tracker: By using templates, selected fields of a defect ticket can be prefilled by information available in **test.guide**.

It is possible to specify a template for each free text field ((as specified by the issue tracker) of a ticket. A template can contain static text, but also placeholders that are replaced with information, for example, from the review or the underlying test case execution (e.g. a certain global constant). A description of supported placeholders can be found on the configuration page.

Currently, issue tracker templates are only supported for Jira.info

This avoids mistakes when creating the ticket and minimizes the coordination effort.

#### 4.6.1.1. Specific template fields

Multi input fields

For fields, that allow multiple values, more than one value can be defined in the template. To separate the values, use the separator sequence `|||`.

Jira Asset fields

Templates for custom fields that contain Jira Assets objects or references must be filled with the key (not the name) of an existing asset. If you e.g. want to reference an Jira Asset "my Tool" with the key "TOOL-1", please fill the template so the value of the field resolves to "TOOL-1".

## 4.7. Management tools

→ <u style="color: blue;">**Management tools**</u>

**test.guide** is the linking element between test execution and test management.

After the review of test case executions has been completed, it is a common task to transfer back the current status to the test management tool. Therefore, different test management tools can be integrated into **test.guide**.

More information about the supported test management tools (or Application Lifecycle Management (ALM) tools) and possibilities can be found at <u style="color: blue;">**Integrating test management tools**</u>.

## 4.8. Upload Rules

→ <u style="color: blue;">**Upload rules**</u>

One of the major challenges, especially for test case coverage calculation, is to ensure consistent metadata for the test case execution reports in the project. Therefore, upload rules can be defined, which ensure that specific required metadata (for example the requirement ID) must be present in each test case report - otherwise, the upload will be rejected.

In addition, the <u style="color: blue;">issue tracker</u> JIRA also offers the possibility to automatically update related tickets when uploading test reports.

## 4.9. Report remove rules

→ <u style="color: blue;">**Report remove rules**</u>

Using test.guide over a period of time can leave you with a lot of reports. Some of which may be no longer needed as they are not assigned to a locked release, probe runs or simply outdated. To keep your database clean of those reports you can set up rules that are applied automatically every evening between 8 pm and midnight. A rule will search for all reports older than x days and filter those not contained in any locked release. The resulting reports are then deleted together with associated reviews and files.

## 4.10. Recycle bin

→ <u style="color: blue;">**Recycle bin**</u>

Use the recycle bin to remove unnecessary attributes and constants from test case executions to reduce the database size and filtering workload. This is a two-step process: First, the unnecessary data must be moved to the recycle bin using the *Move to Recycle Bin* dialog. Then you can permanently delete or restore the items in the recycle bin using the appropriate buttons.

Recycle bin actions are processed as background tasks and can take some time depending on the amount of data. While a task is processed, it is not possible to start further operations for consistency reasons.

## 4.11. ecu.test settings

→ <u style="color: blue;">**ecu.test**</u>

The **ecu.test** ATX Generator settings can be configured centrally via the page. If the configuration is activated, all ATX Generator settings except the connection settings are synchronized and applied with the **test.guide** configuration before the ATX report generation in **ecu.test**.

To allow ecu.test to be managed centrally the ATX Generator settings *useSettingsFromServer* must be activated in the **ecu.test** workspace.error

## 4.12. Project filters

→ <u style="color: blue;">**Project filters**</u>

This page contains a list of all existing project report filters. For each filter, you can see the amount of subscriptions that have been created. It is possible to create new subscriptions (also simultaneously for multiple users) and delete existing subscriptions.

When creating or deleting filter subscriptions, the affected users do not get notified.info

## 4.13. Notify users

→ <u style="color: blue;">**Notify users**</u>

For project announcements, for example when new <u style="color: blue;">upload rules</u> are put into action, it is possible to notify all registered project users via email.

To be able to use this feature the <u style="color: blue;">**Email**</u> settings must be configured. If this is not the case, please ask your admin for help.info

## 4.14. Transfer setup

→ <u style="color: blue;">**Transfer setup**</u>

If a second **test.guide** instance or project is to be set up and you want to transfer and re-use current project settings, this is possible via *Transfer setup*. Using this feature, a backup of current project settings can be made, while at another **test.guide** project, this backup can be imported again.

It is only possible to import the backed-up settings if the same **test.guide** version is used.error

## 4.15. Dashboard views

→ <u style="color: blue;">**Dashboard views**</u>

In the project team, you often want a quick overview of the current test case execution status of specific software variants or special test sections. With the help of the dashboard widgets it is possible to create different dashboards for the wanted overviews in the project.

The dashboard widgets in use are based on the project filters and are updated for the live view at specific time intervals.info

This section provides an overview about the **system configurations** that are important for operating **test.guide**.

## 5.1. General

→ <u style="color: blue;">**General**</u>

General operating settings for **test.guide** are configured in this section.

- Logging
- Application base URL
- Upload buffer
- DoS API access protection

It is important that the application base URL is set up correctly. Otherwise e.g. links in sent emails or in PDF reports created by **test.guide** will not work correctly.error

## 5.2. Database

→ <u style="color: blue;">**Database**</u>

The report database for all test case execution imports can be operated with different database systems. We **recommend using the PostgreSQL database**.

For additional information on setup, see the <u style="color: blue;">Operations Manual</u>.

## 5.3. Monitoring

→ <u style="color: blue;">**Monitoring**</u>

A database must be configured for the recording of test bench data by the **ResourceAdapter**.

The monitoring database for all test bench data (PC vital data, test executions, test bench configuration, ...) can be operated with different database systems. We **recommend using the PostgreSQL database**.

For additional information on setup, see the <u style="color: blue;">Operations Manual</u>.

## 5.4. Authentication

→ <u style="color: blue;">**Authentication**</u>

test.guide supports different authentication methods for authenticating users to the test.guide and the company.

### 5.4.1. Internal User Management

Users can be created with the internal user management.

User names must be unique.error

Users may modify or update their own profiles, except for permissions and the user name.

### 5.4.2. LDAP

To determine the LDAP parameters used in your company's environment, we recommend using the following Microsoft tool: [Active Directory Explorer (AD Explorer)](https://technet.microsoft.com/en-us/sysinternals/adexplorer.aspx).lightbulb_2

To enable LDAP, the following fields must be filled by the responsible IT staff member.

Host

to LDAP server

Port

to LDAP server

Use SSL

SSL (be aware that the certificate must be stored in the Java installation)

Use TLS

TLS

Manager DN

- a user with read permissions on the LDAP server, which will be used to lookup for users to be used in test.guide
- this requires the full LDAP path to be entered
- cn=anonymous,..., dc=local may be used to login without Manager DN

Manager Password

password for Manager DN user (optional)

User Organization Unit

LDAP path in which users are looked up (optional)

User Domain Component

domain in which users are looked up

User ID Attribute

- the LDAP attribute which should be used as login name
- e.g. sAMAccountName, uid or even mail
- this attribute will be mapped to the user name for authentication at login

For each LDAP account to be used in conjunction with test.guide there has to exist a corresponding test.guide user. This user needs a user name matching the value of the User ID Login Attribute.error

### 5.4.3. OpenID Connect

When this option is selected, test.guide acts as an OpenID Connect Relying Party and can authenticate users which are managed by an OpenID Provider.

- test.guide must be statically registered at the OpenID Provider. The credentials obtained in the process (Client Identifier and Secret) must be entered in test.guide's OpenID Configuration dialog.
- test.guide uses OpenID Connect Discovery to obtain the OpenID Provider's metadata
- test.guide uses the Grant Type *"Authorization Code"*
- The Redirection URI is `<test.guide Base URL>/api/oidc/authn-response`. It is also shown in the OpenID Configuration dialog.
- test.guide supports the following authentication methods for the Token endpoint: `client_secret_basic` and `client_secret_post`
- by default test.guide requests the following scope values: `openid`, `profile` and `email`
  - if additional scopes should be requested, please specify them in test.guide's OpenID Configuration
- test.guide uses the following claims from the UserInfo response: `preferred_username`, `name` and `email`
- test.guide supports Front Channel Logout. The URL is `<test.guide Base URL>/logout`.

## 5.5. User Management

→ <u style="color: blue;">**User management**</u>

As server manager all registered users including their project assignment can be managed here.

### 5.5.1. The special user ServerAdmin

The user *ServerAdmin* is a reserved user that has unrestricted access. This user will always have unrestricted access to the application.

The *ServerAdmin* password was set during the setup of test.guide.lightbulb_2

### 5.5.2. Global permissions

Global permissions are permissions that are related to operations that affect the entire **test.guide** instance (as opposed to <u style="color: blue;">project permissions</u>, which are related to a specific project and granted within the respective project setting section, see <u style="color: blue;">**Project users**</u>).

The following global permissions exist and may be assigned to any user:

| Permission | Description | API value |
|----|----|----|
| Server manager | Allows the user to manage the system, giving access to most options of System configuration section (see details of other global permissions for exceptions). | SERVER_MANAGER |
| User management | In combination with *Server manager* permissions, this allows managing users in a global context (adding and deleting users, configuring the employee directory, system groups and system group synchronization). Details about that can be found in the upcoming sections. | USER_MANAGEMENT |
| Metrics access | Allows the user to access usage metrics. | METRICS_ACCESS |

### 5.5.3. Manage users in global context

A user with *User Management* permission can access the menu at <u style="color: blue;">**User management**</u>, where all users are listed. It is possible to create both regular and technical users at this page. After creation, a user account does not have any projects assigned.

The user list supports the following operations:

| Action | Description |
|----|----|
| Edit | Change the user's profile and/or global permissions. |
| Projects | Assign or remove a user to/from a project. This will open a new page listing assigned projects. |
| Delete | Deletes the user permanently, also deleting all project assignments. |

### 5.5.4. Wipe out username

If a colleague leaves the company or project it is possible to make his user name anonymous in **test.guide**.

Look at <u style="color: blue;">**User management**</u> for **Wipe out username**.

### 5.5.5. Configure disclaimer

When this button is pressed, a new page will be opened that is intended to publish and manage disclaimers.

A disclaimer is (in the context of test.guide) a compliance-related tool intended to require users to take note of and accept the terms that are written down in the disclaimer text.

<figure>
<img
src="test.guide%20user%20documentation-media/07fc27571ddd0c8424ecde287a180688d1d93b6f.png"
alt="83fa8d91e6c6c40c6d12a6bcabaae50b_MD5" />
<figcaption
aria-hidden="true">83fa8d91e6c6c40c6d12a6bcabaae50b_MD5</figcaption>
</figure>

DisclaimerResult

The feature is characterized as follows:

It is not possible to edit or remove a disclaimer once it is published!warning

- only one disclaimer is valid at a time
- disclaimer history on **Configure disclaimer** page also shows old disclaimers, which are not valid anymore
- users must accept the current disclaimer, this is checked when they try to log in
- if a user accepts the disclaimer, he will not be prompted again until a new disclaimer is published
- if a user does not accept the disclaimer, he will not be able to log in
- when exporting the user list, the *Confirmed disclaimer version* column contains the disclaimer version confirmed by the user

The disclaimer can be formatted using HTML tags as needed.lightbulb_2

## 5.6. System groups

→ <u style="color: blue;">**System groups**</u>

A user can be a member of any number of system groups. A system group can be associated with different project roles for each project, giving the user the appropriate permissions in a project. If the roles include permissions for a project to which the user is not yet a member, the user is automatically added and enabled as a project member. In this case, the project managers are notified by email.

System groups are either synchronized to the user based on LDAP user groups or OpenID Connect roles.

At **System groups** server managers can find an overview over all imported system groups and their members. When during synchronization a new system group is found, it will be added to this view.

If server managers want to configure project roles for a system group that has not been synchronized yet, they can also add system groups in advance by using the *Create new system group* button on the page. Group members will be added later through synchronization. For synchronization to work, the group name must be written exactly like it would be provided by either LDAP or OpenID Connect synchronization.info

Existing system groups are not removed automatically. They can be deleted by server managers. If there are still members of the group, the group will be re-created the next time their data is synchronized, but the assigned roles can not be restored.

The synchronization needs to be configured at <u style="color: blue;">**System groups**</u> page, by hitting the *Configure synchronization* button. The following sections explain how the configuration must be carried out for the different mechanisms and highlight any specific requirements that apply:

### 5.6.1. Using LDAP system group synchronization

User groups of LDAP can be used to create system groups in test.guide. The name of a system group is the full LDAP path of the group.

This feature can be used regardless of whether LDAP is also used to authenticate users or not. For example, synchronization of the system groups via LDAP is also possible if OpenID Connect is the used authentication method. However, the prerequisite is that the users can be located in the LDAP directory via their **test.guide** user name.lightbulb_2

At the *Configure system group synchronization* page, select *LDAP* as synchronization mechanism. Next, please specify the configuration that can be used to connect to the LDAP server and locate the users in the directory. The chapter on how to configure <u style="color: blue;">LDAP Authentication</u> may provide helpful information on how to do this. Additionally, the following fields are important:

Attribute containing the system groups

the LDAP attribute whose values should be interpreted as user groups, e.g. "memberOf"

Path suffix for system group selection

if a value is entered, only groups whose LDAP paths end with the given DN are imported

When the synchronization is enabled, the LDAP groups of a user are retrieved on login. Additionally a background service updates group informations for all known system users hourly. If a user is added to a group in LDAP, on next synchronization they will become a member on the respective system group in test.guide.

### 5.6.2. Using OpenID Connect system group synchronization

Only in case OpenID Connect is used to authenticate users in test.guide, it can also be used to create system groups based on a users OpenID Connect access token claims.

Please note that due to the characteristics of OpenID Connect, synchronization can only take place when a user logs in. Automatic synchronization of all users at regular intervals, as is possible with LDAP, is not possible with OpenID Connect.error

If additional scopes should be requested from the OpenID Connect provider, because they contain necessary group information, please add the respective scopes to the authentication config at → <u style="color: blue;">**Authentication**</u>.lightbulb_2

This feature can be enabled at <u style="color: blue;">**System groups**</u> by hitting the *Configure synchronization* button. On the page that opens, select *OpenID Connect* as synchronization mechanism and provide one or more valid JsonPath expression to extract the system group names from the access token and / or the user info response the OpenID Connect provider hands over to test.guide during user authentication.

The following information is only intended as a reference, the actual structure of the Access Token and the JsonPath expressions required with it depends heavily on the respective infrastructure and must be specifically adapted to this.info

The following snippet shows an excerpt of a typical access token:

``` json
{
  "realm_access": {
    "roles": [
      "offline_access"
    ]
  },
  "resource_access": {
    "account": {
      "roles": [
        "hil_user",
        "tg_admin"
      ]
    }
  }
}
```

Based on this excerpt, the following examples show valid JsonPath expressions to create system groups based on the roles of this access token:

- `$['realm_access']['roles'][*]` - this will import only the `offline_access` role as a test.guide system group
- `$['resource_access']['account']['roles'][*]` - this will import both the `hil_user` and the `tg_admin` role
- `$..['roles'][*]` - this will import all array values of every `roles` object, in this example `offline_access`, `hil_user` and `tg_admin`

The same is applicable for the user info response, which is also a JSON object and may have an array containing the system group names.

For details on JsonPath syntax please consult [this resource](https://github.com/json-path/JsonPath). There also exist tools to interactively try out JsonPath expressions, which can be a good way to find the correct expression for your own access token.lightbulb_2

## 5.7. Project management

→ <u style="color: blue;">**Project management**</u>

With test.guide it is possible to manage multiple projects.

When creating the project, the project manager must be specified. If the *Project Manager* is not yet available as a user in the **test.guide**, then the *Server Manager* should also be entered as *Project Manager* and the user should be assigned after registration.

The project managers can then manage their project at <u style="color: blue;">menu:Project settings</u>.

We recommend to always have at least two project managers, so that a stand-in is guaranteed in case of, for example, illness or vacation.lightbulb_2

### 5.7.1. Disable and delete projects

A *Server Manager* can disable a project at → <u style="color: blue;">**Project management**</u>. When a project is disabled, it is not possible to view or change any data in the project, to change permissions within the project or to apply for membership. A disabled project can be re-enabled at any time.

To delete a project, it has to be disabled first. Afterwards, a *Server Manager* can request its deletion. When requesting project deletion, one has the choice to specify that **test.guide** also removes data stored in the projects file repositories and upload buffer. Use this option if you want to remove a project completely. However, if the data is still accessed from elsewhere (e.g. if the project was moved to another **test.guide** instance, but using the same storage for the repositories), this option should be left unchecked.

Deleting the data of the project might start with some delay, as it is performed by a background job.

Once project deletion has been requested, this operation cannot be cancelled. Deleting a project is irreversible.warning

## 5.8. Email

→ <u style="color: blue;">**Email**</u>

test.guide offers several features which use email communication to notify users of new results or important events. This includes the following features:

- User registration: Users with *User management* permission get notified if a new user requests registration. The user who requested registration gets notified in case his request was accepted or declined.
- License reminder: Prior test.guides license expires, a warning is sent to *Server management* users.
- Notify users: *Server management* users may send a notification to all users who have their email address set, for example to inform them about upcoming maintenance work or downtimes.
- Filter subscription: At **Report filter** page a user may create a subscription, which automatically executes the given filter in four-hour intervals and sends a notification if new results were found.
- Test case subscription: At **Test case detail** page a user may create a subscription, which checks in five-minute intervals if new results exists for this test case. In this case a notification is sent.
- Test case coverage subscription: At **Coverage filter** page a user may subscribe to a coverage filter, which will be executed automatically in intervals of 24 hours. The results will be sent to the user by email.
- Test summary report: Because the creation of test summary reports can take some time, it is possible to let them run as a background task. The resulting PDF file will be sent by email.

### 5.8.1. Email configuration

To use these features a SMTP server must be configured which delivers outgoing mails. This configuration is possible via the page **Email**. At this page it is necessary to check *Activate email* and fill out the form according to the configuration of the SMTP server which is to be used.

Additionally, the value of the field *Application base URL* has to be set to the URL test.guide currently is accessible at. For example, this may be *[https://localhost:8443](https://localhost:8443/)* if the application is running locally and HTTPS is enabled. This value is used for linking to the web application: If it is not set correctly, the links embodied in mails sent by the application may not work.

By clicking the **Save** button the changed configuration will be enabled.

It is possible to send a test email to a certain recipient by filling the address field and clicking the **Send** button at the bottom of the configuration page.lightbulb_2

### 5.8.2. Setting email addresses

The above features will only work for users whose email addresses are set.

This can be done in two ways:

- A administrative user, who has the permission *User management* (see <u style="color: blue;">**User management**</u>), may add or change email addresses of other users.
- Each user may add an email address on his own by clicking on the user name at the down left of the navigation section and selecting **Edit profile**. The page opened allows to add an email address for the current user.

## 5.9. Notify users

→ <u style="color: blue;">**Notify users**</u>

For announcements in the form of e.g. maintenance work it is possible to inform all

- registered **test.guide** users
- or only selected project groups

via mail.

To be able to use this feature the <u style="color: blue;">**Email**</u> settings must be configured.info

## 5.10. Transfer setup

→ <u style="color: blue;">**Transfer setup**</u>

If a second **test.guide** is to be set up and you want to take over the settings and users, it is possible via *Transfer setup* to make a backup of the current settings and import them into the second empty test.guide.

The transfer of the backed-up settings is only supported for **test.guide** s with identical versions!error

## 5.11. System status

→ <u style="color: blue;">**System status**</u>

This page provides:

- an up-to-date overview of the vital status of the server
- the project setups
- and server settings

## 5.12. Maintenance mode

→ <u style="color: blue;">**Maintenance mode**</u>

This page allows to enable or disable the *maintenance mode*, which is useful to inform users that **test.guide** is not available for a while (for example when moving from one database server to another) and will not accept results.

While **test.guide** is in maintenance mode, all users without the *Server Manager* permission will not be able to use the application through the browser or API. Instead, they will be redirected to a page informing about the maintenance being in progress.

Furthermore, requests to the applications APIs will not be processed in the usual way, but are responded to with the HTTP status code `503 Service unavailable`. This response will contain a `Retry-After` header, which suggests the client to retry its original request after a certain time span, which can be specified when enabling the maintenance mode.

To return to normal operation, any user with the global permission *Server Manager* may return to <u style="color: blue;">**Maintenance mode**</u> page and disable the maintenance mode.

## 5.13. Backup

→ <u style="color: blue;">**Backup**</u>

Configure backup of all uploaded reports to a SMB storage:

In a worst-case scenario the database can get corrupted or fails without a database backup (which is strongly recommended) to restore. To somehow reduce the impact of such an event **test.guide** can copy every incoming report to a remote storage.

The *Retention time* option specifies how long these backed up reports are kept.

If your DBMS is configured to create snapshots of the **test.guide** database bi-weekly, it is reasonable to choose the retention time setting to reflect this and provide an additional buffer. Hence, a value of 15 days would be appropriate to handle the period between automatic database backups.lightbulb_2

### 5.13.1. Restoring backed up reports

Clicking *Begin backup restore* opens a dialog that allows to restore backups from a specified time period. The restore status may be supervised using the *Task manager*, it is listed there as a *System task*.

The dates entered are considered inclusive, for example, specifying *Mar 20, 2021* to *Mar 22, 2021* will restore three full days worth of reports.info

Restoring backups may also be done in *Maintenance mode*.lightbulb_2

## 6 Customizing

Learn how to customize **test.guide** according to the needs of your project.

## 6.1. Customizing project with dashboards

You can customize the home page of your project by using **dashboards** in **test.guide**.

To do so you first need to create a new dashboard at <u style="color: blue;">**Dashboard views**</u>. At first creation you have to specify some parameters like the name of the dashboard and the refresh period. You can also add widgets and arrange them within the specified columns by using drag and drop. Some widgets are based on a saved report filter. So if you want to use one of these widgets and you don't have any saved filter definitions please add one beforehand.

Existing dashboards can be edited as well at this page.lightbulb_2

To set a configured dashboard as the home page of your project, you need to activate the option "As home page" in the dropdown menu on the settings page ( <u style="color: blue;">**Dashboard views**</u>). Only one dashboard can be set as the home page. This dashboard will also be shown at first when entering the Dashboard-page and by clicking on **Home page**. When there is no home page dashboard defined, a project statistics will be displayed at this place.

After creating a dashboard, all available dashboards of a project become accessible in the menu bar under **Dashboards** on the left.lightbulb_2

## 6.2. Customizing the report filter

The report filter page of a project can be customized at <u style="color: blue;">**Filter settings**</u>, allowing to define individual settings for each **test.guide** project.

Various customizations may be performed:

- The default view of report filter page can be defined.
- The filter field labels can be customized by replacing the default value.
- Filter fields may be rearranged using the dialog opened by clicking the **Sort filter** button.
- Filter fields are arranged in filter groups, which also are customizable:
  - It is possible to rename existing filter groups.
  - New filter groups can be created by using the **Add group** button in the drop-down menu.
  - Filter groups can be rearranged using the **Sort filter** button.
- Furthermore, **custom filter fields** can be added by using the drop-down menu, which allows to provide a project-specific view on chosen attributes or constants, thus effectively simplifying the use of the report filter.

## 6.3. Customizing the PDF export

When creating PDF reports, e.g. by using the report filters export view or by using the export menu of the coverage filter, a powerful template engine is used to create the resulting PDF document. This engine is part of the **Business Intelligence and Reporting Tools** (BIRT) developed by the Eclipse Foundation, which uses so called *report designs* as templates.

**tracetronic** provides *default report designs*, which are delivered alongside **test.guide**. Nevertheless, it may be desirable to adapt these templates to your own needs or to develop new report design from scratch.

The *default report designs files* are distributed as an integral part of tracetronic's test.guide software and may only be used in connection with and pursuant to the terms and conditions of a valid test.guide license. Copyright © by tracetronic GmbH, Dresden

info

BIRT is a powerful and complex framework, hence intense and self-dependent training on its usage is strongly recommended. The following description is intended to explain the specific aspects and recommendations of the interaction between **test.guide** and BIRT. For general questions about report designs, please refer to the BIRT documentation. Please note that implementing data access also requires knowledge of SQL.warning

### 6.3.1. Setting up the BIRT Report Designer IDE

Report designs are developed using the **Eclipse BIRT Report Designer**. We recommend using the *Report Designer All In One* package available here: [eclipse.org (External link)](https://download.eclipse.org/birt/updates/release/4.20.0/index.html)

Recommended version of the Report Designer is `4.20.0-202506110821`. Windows users may use the bundle found under the filename `birt-report-designer-all-in-one-4.20.0-202506110821-win32.win32.x86_64.zip` on the above page. The *all-in-one* version includes the required `Java SE 21` runtime (for more details see the readme_eclipse.html contained in the mentioned download).error

With this application report designs can be created, edited and (if a data source is connected) also <u style="color: blue;">tried out</u>.

- Download the Report Designer and unzip the archive to a location of your choice.
- Start the executable contained (Windows users want to start `birt.exe`).
- When prompted, create a new workspace.

Because **test.guide** hands over data to BIRT using a temporary **H2 database**, the corresponding database driver must be obtained as well.

The required database driver version for up-to-date report designs is **2.4.240**. Please visit [h2database.com (External link)](https://h2database.com/html/download.html) and use the *2.4.240 Platform-Independent Zip* link to download it.error

- Open the downloaded ZIP file and inside, navigate to `\h2\bin\`.
- Extract the file `h2-2.4.240.jar`, for example into the folder you extracted BIRT Report Designer to.

Your setup is now ready to being used. In the following section you will learn what qualifies a valid report and how to use the database driver for accessing a data source.

### 6.3.2. Customizing existing report designs

All existing report designs, including the default report designs provided by **tracetronic**, are available for download at <u style="color: blue;">**Reporting**</u>. These report designs can serve as a starting point for modifications.lightbulb_2

- Start the BIRT Report Designer and create a new report project by clicking **File** **New** **Other** **Business Intelligence and Reporting Tools** **Report Project**.
- Copy the existing base report design into this project. It is recommended to give the copied report design a meaningful name.
- Open the report design within the Report Designer.

Next, the data source must be configured:

- In the **Data Explorer**, open the `TEST-GUIDE_DataSource`.
- It is important, that the database driver (see <u style="color: blue;">Setting up the BIRT Report Designer IDE</u>) of this data source is set up correctly:
  - To do so, open the data source configuration (e.g. by double clicking it) and click the **Manage drivers** button.
  - In the `Manage JDBC Drivers` dialog click **Add** and choose the JAR file of the H2 database driver.
- Modify the report design according to your needs. You may want to <u style="color: blue;">try it out</u> while doing so to check if the modifications made are correct.
- After finishing modification, save the report design file and upload it to **test.guide** at <u style="color: blue;">**Reporting**</u>.

If the desired structure and content of the PDF is very different from existing report designs, it may make sense to create a report design from scratch. When doing so, it is important not to forget about the prerequisites mentioned at <u style="color: blue;">Report design requirements</u>.error

### 6.3.3. Trying out report designs during development

During report design development it is necessary to continuously check whether the latest changes work correctly. In order to avoid having to upload the report design to **test.guide** and execute it every single time, one can specify a fixed "example" data source in the report design, which is used by the Report Designer. By doing so, developing report designs is possible even without access to **test.guide**.

The following procedure can be used to create a suitable "offline" data source and use it during report design development:

- In **test.guide**, depending on the type of the report design, calculate either a suitable report filter or coverage filter.

The filter used should be similar to the one that will be used with the report design in production, but it is reasonable to limit the amount of data.lightbulb_2

- Open the dialog for exporting a PDF and select any existing report design.
- Before starting the export, it is important to enable the option ☑ **Include report data source in download**.
- Wait for the process to finish and download the ZIP file created.
- Open the ZIP file and extract the file with extension `.mv.db`. It is recommended to put the file next to the file of the report design under development.
- In BIRT Report Designer, open properties for the primary data source called `TEST-GUIDE_DataSource`.
- Modify the database URL so it points to the database file.

Please note that the URL must be a valid JDBC URL and that the file extension of the data source must not be specified.info

If not already done, refer to <u style="color: blue;">Report design requirements</u> on how to setup the JDBC driver.error

Now, when using the preview tab of a data set or when clicking the **Run report** button in BIRT Report Designer, data is fetched from this data source.

Regardless of the database URL setting in data source properties, **test.guide** will always use real data when using the report design in production.info

### 6.3.4. Report design requirements

For a report design to be compatible with **test.guide**, it must meet a number of requirements. If you are creating a new report design from scratch, please make sure it meets the requirements described in this section. If instead you are modifying the default report design provided by **tracetronic**, these requirements are already met, but you may want to customize the report properties listed below.

#### 6.3.4.1. Data source

Every report design must contain a `JDBC Data Source` named `TEST-GUIDE_DataSource`.

This primary data source is a fundamental element of the report design. It is the single point of data access and provides a link between the report and the rich data stock of **test.guide**.info

#### 6.3.4.2. Report properties

In the root element of the report design (select it by clicking on the upper entry in the outline view of the *Report Designer*), by using the *Property Editor*, some settings must be made. These settings are used to manage the report designs in **test.guide** and ensure that the report design can be processed correctly.

- Tab **General**, property `Author`: The author of the report design or, if applicable, a department or company should be entered here.
- Tab **User Properties**: Three user properties of type *String* with the names `DataSourceSpec`, `ReportDesignType` and `Version` must be created here.
- Tab **Advanced**: The previously mentioned user properties can be found in this list and their value should be set meaningfully:
  - `DataSourceSpec` tells **test.guide** which format the primary data source expects. Currently, the default report designs use `H2_2.0.0`. Legacy support for older report designs using `H2_1.0.0` is still available, but will be discontinued after prior notice.
  - `ReportDesignType` tells **test.guide** the type of the report and thus decides, in which context the report design can be used. Valid values: `TEST_SUMMARY_REPORT` (used at report filter), `TEST_COVERAGE_REPORT` (used at coverage filter)
  - `Version`, like the Author property, can be entered freely. Its value is displayed in **test.guide** when managing and using report designs. For keeping track on report designs, it is recommended to maintain a semantic versioning, possibly combined with a date (e.g. `1.0.1 (2020-03-18)`).

### 6.3.5. Migration guide

Starting with version 1.211.0, **test.guide** uses a new version of the H2 database driver to benefit from improved functionality and security. The updated database is not backward compatible with the existing version.

As a consequence, to take advantage of the capabilities of the updated database and remain compatible in the future, it is highly recommended to migrate the custom report designs to the new version of the `DataSourceSpec`. See section <u style="color: blue;">Migrating an existing report design</u> on how to do this.

If migration is not currently feasible, unmigrated report designs may still be used. In this case, they will be executed in compatibility mode. However, the compatibility mode may be discontinued at a later point. If changes are to be made to such a report design without migrating it, it is important to pay attention to the requirements mentioned in section <u style="color: blue;">Continue editing outdated report designs without migration</u>.

#### 6.3.5.1. Migrating an existing report design

The following assistance is based on the report designs known to us. However, all conceivable SQL queries can occur in the data sets of the custom report designs, which means that it is not possible to list all potential problems. It is therefore recommended to thoroughly check the generated PDFs for correctness and completeness after migration.error

###### Breaking changes

Related to new H2 database version

Previous version: 1.4.199, Updated version: 2.4.240

- More reserved keywords and stricter treatment of conflicts with identifiers (like for example column names).
- Disallowance of unsafe comparison between numeric and boolean values.

In addition to these two changes, which are the most prominent, there are mainly changes affecting non-standard SQL syntax: Some previously supported, vendor-specific syntax is no longer supported with H2 2.4.240 and must be replaced by standard SQL.warning

Related to new DataSourceSpec version

Previous version: `H2_1.0.0`, Updated version: `H2_2.0.0`

To avoid conflicts with reserved keywords, the following table columns were renamed within the database:

| Affected table | Old column name (`H2_1.0.0`) | New column name (`H2_2.0.0`) | Remarks |
|----|----|----|----|
| `TCE_ATTRIBUTES` | `VALUE` | `ATTRIBUTE_VALUE` |  |
| `TCE_PARAMETERS` | `VALUE` | `PARAMETER_VALUE` |  |
| `TCE_CONSTANTS` | `VALUE` | `CONSTANT_VALUE` |  |
| `TCE_ENVIRONMENT_CONFIG` | `VALUE` | `TESTENVCFG_VALUE` |  |
| `SCOPEMAP` | `VALUE` | `SCOPE_VALUE` | only used in test coverage reports |

###### Procedure

Create a backup

It is highly recommended to keep a backup of the report design that is about to be migrated. Using a version control system is a good practice to do so.

Prepare the Eclipse BIRT Report Designer

- Download and prepare the recommend H2 database driver JAR file, see section <u style="color: blue;">Setting up the BIRT Report Designer IDE</u> for details
- Open the custom report design within the Report Designer and open the dialog to edit the `TEST-GUIDE_DataSource`
- In the **Edit Data Source** dialog, click **Manage Drivers**
- In the **Manage JDBC Drivers** dialog, remove the existing entry of the old H2 database driver
- Next, click **Add** and select the previously downloaded H2 database driver

Adjust the report design metadata

- Open the **Property Editor** for the root element of the report design (e.g. by click the report design name in the **Outline** view)
- In **Property Editor**, switch to the **Advanced** tab
- Edit the value of the `DataSourceSpec` property to the following: `H2_2.0.0`
- Recommended: Still in the **Advanced** tab, update the `Version` property to a new version. This helps keeping track of changes in **test.guide**.

Adjust the report design data sets

For custom report designs that are adapted versions of the default designs provided by **test.guide**, the migration script [migrate_birt_template.py](https://testguide.one-cx.cn/help-docs/060_Customizing/files/migrate_birt_template.py) is available. This script automatically adapts the SQL queries for changed column names, but it is strictly limited to report designs that still use the original data sets in an unchanged way.lightbulb_2

In all data sets:

- Check for identifiers that conflict with reserved keywords and either rename them or escape them using double quotation marks.
- Check for any old column names and replace them with the new ones listed in the above table.

Renaming columns can be inconvenient: The report designer will not automatically propagate the new name to all the places where the data set was previously used, meaning widespread manual adaptations will be necessary. Therefore, it may be easier to use the following method, as demonstrated by the altered column name in the `TCE_CONSTANTS` table: `SELECT CONSTANT_VALUE AS "VALUE" FROM TCE_CONSTANTS;`

This query will use the correct new column name `CONSTANT_VALUE`, but by using the `AS` keyword it will make them available to the places using the data set via the old name, `VALUE`. The double quotation marks used will prevent the conflict with the reserved SQL keyword.

Depending on the custom SQL queries used in the data sets, more adaptations may be necessary, given that the syntax of the new H2 database version has changed compared to the previous one.error

Check the results

Since there may be other compatibility issues that would not result in an error message when using the report design in **test.guide**, it is important to check the report design for functionality using the Report Designer. To do so:

- As the described in section <u style="color: blue;">Trying out report designs during development</u>, create a data source containing a meaningful set of data and set it up as the `TEST-GUIDE_DataSource` within the Report Designer.
- To get a preview of the PDF, use **As PDF**. Check the PDF for correctness and completeness.
- In the Report Designer, open the **Problems** view and check if any errors are listed. If so, check the error message, as it may provide information on any remaining incompatible SQL queries.

#### 6.3.5.2. Continue editing outdated report designs without migration

It is not recommended to continue using outdated report designs that rely on the old `DataSourceSpec`. They will run in compatibility mode, but support for these types of report design may be subject to deprecation.warning

**test.guide** uses a fork of the original H2 database driver to provide compatibility to legacy report designs that were created using H2 database version 1.4.199.

The forked database driver, including the source code, is available for download: [h2-2019-03-13.zip](https://testguide.one-cx.cn/help-docs/060_Customizing/files/h2-2019-03-13.zip)

To avoid conflicts with the regular version 2.4.240 of the database driver, the following adjustments were made in the forked driver:

- The forked database driver is known as `org.h2v1_4_199.Driver`.
- The forked database driver requires the JDBC URLs to beginn with `jdbc:h2v1_4_199:`.

Instructions

When editing outdated report designs within the Eclipse BIRT Report Designer, these changes must be adhered to:

- The forked driver must be registered within the Eclipse BIRT Report Designer.
  - The procedure is the same as described in section <u style="color: blue;">Setting up the BIRT Report Designer IDE</u>, but use above link to download the forked legacy driver (instead of the 2.4.240 one) and use the `h2\bin\h2-1.4.199.jar` file contained in the downloaded ZIP file.
- The `TEST-GUIDE_DataSource` must be configured to use the forked driver.
  - Open the **Edit Data Source** dialog and set the **Driver class** (using the drop-down list) to the new entry `org.h2v1_4_199.Driver (v1.4)`.
  - When supplying the **Database URL** of an example data source (to use for previews etc.), remember to use the URL prefix `jdbc:h2v1_4_199:`, e.g. enter `jdbc:h2v1_4_199:/home/johndoe/BIRT/DownloadedReportDataSource;`.

## 7 Developing

This section contains information for developers who want to use the API to automate processes or develop new applications based on the API.

## 7.1. REST-API

The API is a Representational State Transfer (REST)ful web service that provides a simple, user-friendly interface through standard HTTP request and response messages. **The REST API documentation including a tryout environment for the API is available at [/api-docs](https://testguide.one-cx.cn/api-docs).**

## 7.2. Checking server readiness

API calls can only be successful if the **test.guide** server is ready, i.e. it is fully started up and all database connections are established. Via the [Health API](https://testguide.one-cx.cn/api-docs/?urls.primaryName=Health%20API), **test.guide** exposes a REST endpoint that allows clients to check for server readiness before using the API. The following Python script demonstrates how to query the endpoint and wait for **test.guide** 's readiness:

``` python
# -*- coding: utf-8 -*-
import requests
import time
from datetime import datetime

baseUrl = r'https://your.test-guide.instance:8443'  (1)

def sleep(retryAfter):
    '''
    Blocks until the specified retry-after point in time is reached.
    :param retryAfter: Value of the Retry-After HTTP header
    :type: str
    :return: None
    '''

    if not retryAfter:
        print("Server didn't send a Retry-After header, using default value")
        sleepSec = 60
    elif retryAfter.isdigit():
        sleepSec = int(retryAfter)
    else:
        # RFC 1123 format: Thu, 01 Dec 1994 16:00:00 GMT
        dateRetryAfter = datetime.strptime(retryAfter, '%a, %d %b %Y %H:%M:%S GMT')
        dateNow = datetime.now()
        sleepSec = int(dateRetryAfter.timestamp() - dateNow.timestamp())

    print("Retrying after {0} seconds".format(sleepSec))
    time.sleep(sleepSec)

def waitForReadiness():
    '''
    Blocks until test.guide is ready to use.
    :return: None
    '''
    url = r'{0}/api/health/ready'.format(baseUrl)

    ready = False

    while not ready:
        response = requests.get(url, verify=True)

        if response.status_code == 200:
            ready = True
        elif response.status_code in [429, 503]:
            sleep(response.headers.get("Retry-After"))
        else:
            raise Exception("Unexpected response")

    print("test.guide is ready")

waitForReadiness()

# Proceed here with using the API
```

| **1** | test.guide host URL |
|-------|---------------------|

## 7.3. Authentication

To use the API it is necessary to authenticate yourself. This is realized with the *authentication key* and the *project Id*.

You can find out the current *project Id* by hovering over the project at the top of the navigation on the left. Authentication keys can be created and revoked in your profile at <u style="color: blue;">**Auth Keys**</u>.

With the following Python script you can easily check your settings:

``` python
# -*- coding: utf-8 -*-
import requests

headers = {'TestGuide-AuthKey':'nOPVJ3T6JwqUAR8skQ~yourAuthKey~'}  (1)

params = {"projectId": 1} (2)

host = r'https://your.test-guide.instance:8443'  (3)

url = r'{0}/api/releases'.format(host)  (4)

r = requests.get(url, params=params, verify=True, headers=headers) (5)

if r.status_code < 300:
    print("API access successful.")
else:
    print("No API access! Check your settings.")
```

| **1** | User authentication key is provided in the header |
|----|----|
| **2** | Project ID |
| **3** | test.guide host URL |
| **4** | API call: Retrieve all releases of a project |
| **5** | Parameter handling: requests takes care of proper encoding of the parameters |

### 7.3.1. Authentication when using OpenID Connect

When test.guide is configured to use OpenID Connect, it is also possible to authenticate using a *JWT Bearer Access Token* instead of an authentication key. An access token must fulfill the following requirements to be accepted:

- It must be signed by the OpenID Provider that the test.guide instance uses
- Its audience claim (`aud`) must include the Client ID of the test.guide instance at the OpenID Provider
- Its subject claim (`sub`) must identify a test.guide user that has before logged in to the Web interface at least once. Hence, it cannot be a technical user.

It is in the scope of the API client to obtain such an access token from the OpenID Provider. For example, the authorization code flow might be used for that.

For each API request, the API client must provide the access token in the `Authorization` HTTP header using the Bearer scheme.

## 7.4. X2ATX Upload

Via the X2ATX framework, it is easily possible to upload report data in other formats than <u style="color: blue;">**ATX**</u>.

The following is an example for uploading a JUnit report and a Json report to **test.guide**.

``` python
# -*- coding: utf-8 -*-
import os
import requests
import time

class TGReportUploader:

    REQUESTS_VERIFY = True

    def __init__(self, url, authKey, projectId=1):
        """
        Constructor
        :param url: test.guide URL e.g.: https://your.test-guide.instance:8443
        :type url: str
        :param authKey: test.guide upload authentication key
        :type authKey: str
        :param projectId: ID of the test.guide project into which the data is to be
                          imported
        :type projectId: integer
        """
        self.__url = url.strip("/")
        self.__authKey = authKey
        self.__projectId = projectId
        self.__defaultAuthPayLoad = {'projectId':  self.__projectId}

    def UploadBundle(self, path, converter=""):
        """
        Uploads the specified test report bundle to test.guide.
        :param path: Path to the test report bundle to be uploaded.
        :type path: str
        :param converter: Id of the x2ATX converter to be used.
        :type converter: str
        """
        uploadUrl = f"{self.__url}/api/report/reports"

        payload = self.__defaultAuthPayLoad.copy()
        payload['converterId'] = converter

        print('Upload to test.guide:')
        print(f'\tUploading "{path}" to {uploadUrl}')

        headers={
            'Content-type':'application/zip',
            'Accept':'application/json',
            'TestGuide-AuthKey': self.__authKey
        }

        with open(path, 'rb') as file:
            response = requests.post(uploadUrl, params=payload, data=file, headers=headers, verify=self.REQUESTS_VERIFY)

            print(f"\tUpload file status code from test.guide: {response.status_code}")
            response.raise_for_status()

            taskId = response.json().get("taskId")
            print(f'\tUpload is being processed under task id {taskId}.')
            return self.__WaitUntilUploadIsFinished(taskId)

    def __WaitUntilUploadIsFinished(self, taskId):
        headers={
            'Accept':'application/json',
            'TestGuide-AuthKey': self.__authKey
        }
        endpoint = f"{self.__url}/api/report/reports/uploadstatus/{taskId}"
        while True:
            response = requests.get(endpoint, headers=headers, params=self.__defaultAuthPayLoad, verify=self.REQUESTS_VERIFY)
            jsonResponse = response.json()
            uploadStatus = jsonResponse.get("status")
            if uploadStatus == 'finished':
                print(f'\tUpload task {taskId} is finished')
                uploadReturnCode = jsonResponse.get("uploadResult").get("uploadReturnCode")
                msg = jsonResponse.get("uploadResult").get("resultMessages")
                if uploadReturnCode >= 400:
                    print(f'\tUpload failed: {msg}')
                    return False
                else:
                    print(f'\tUpload successfull: {msg}')
                    return True
            else:
                print(f'\tUpload task is not done yet... status: {uploadStatus}.')
                time.sleep(1)

if __name__ == '__main__':
    # test.guide Upload Parameter
    AUTHKEY = "EQmVm00=.RYk1mS21GYNhCQeqaQG0EZsFWENk5VaRsvXrVQGDako="  (1)
    URL = "https://localhost:8443"  (2)
    PROJECT_ID = 1   (3)

    # Upload File
    CUR_FOLDER = os.path.dirname(__file__)
    JSON2ATX_FILE = os.path.join(CUR_FOLDER,"JsonReportWithArtifacts.zip")  (4)
    JUNIT2ATX_FILE = os.path.join(CUR_FOLDER,"junitExample.zip")  (5)

    # x2ATX converter
    JSON_ATX_CONVERTER = "json2atx"   (6)
    JUNIT_ATX_CONVERTER = "JUnitSurefirePlugin"   (6)

    UPLOADER = TGReportUploader(URL, AUTHKEY, PROJECT_ID)
    UPLOADER.UploadBundle(JSON2ATX_FILE, JSON_ATX_CONVERTER)
    UPLOADER.UploadBundle(JUNIT2ATX_FILE, JUNIT_ATX_CONVERTER)
```

| **1** | User authentication key |
|----|----|
| **2** | test.guide host URL |
| **3** | Project ID |
| **4** | [JsonReport2ATX example](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/X2ATX/Uploader/JsonReportWithArtifacts.zip) or use [Basic Json report example](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/X2ATX/Uploader/BasicJsonReport.zip) |
| **5** | [JUnitReport2ATX example](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/X2ATX/Uploader/junitExample.zip) |
| **6** | X2ATX Converter ID specification |

### 7.4.1. X2ATX Converter IDs

The following converter IDs are available:

DEFAULT

for ecu.test ATX report

CANoePlugin

for CANoe reports

cucumber2atx

for [cucumber](https://cucumber.io/) reports

jsonReport

A special JSON test report format. The current JSON schema is available for download at <u style="color: blue;">**Import ATX**</u> after selecting the JSON Report converter. This plugin offers are more comprehensive schema then the old json2atx converter. It also uses a more relaxed pattern for identifiers, such as test case names and constants. For example, it allows these identifiers to include non-Latin characters and to start with a number.

json2atx

A special JSON test report format. The current JSON schema is available for download at <u style="color: blue;">**Import ATX**</u> after selecting the Json2ATX converter. This converter automatically replaces invalid characters in identifiers. It enforces a more restrictive pattern for all identifiers than the newer jsonReport converter does. For example, it excludes non-Latin characters and hyphens.

JUnitMatlab

for [Matlab](https://www.mathworks.com/products/matlab.html) JUnit reports

JUnitSurefirePlugin

for JUnit [maven surefire](http://maven.apache.org/surefire/maven-surefire-plugin/) reports e.g. from Jenkins

NUnit3Plugin

for [NUnit](https://nunit.org/) reports

## 7.5. Artifact management

The artifact management in **test.guide** allows to manage files for testing in an automation-friendly way. This is the reason for the Artifact-API.

### 7.5.1. Upload Artifacts

The following code section shows the parameterization of a example upload artifact script:

- Python script: [UploadArtifacts.py](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/Artifact/UploadArtifact/UploadArtifacts.py)

``` python
# -*- coding: utf-8 -*-
import requests
import os
import json

file = "./ConstructionSite"  (1)
projectId = 1  (2)
depositoryId = "Scenarios1"  (3)
authKey = 'rn~YourAuthKey~'  (4)
host = "https://localhost:8443"  (5)

payload = {}
payload['projectId'] = projectId
payload['depositoryId'] = depositoryId
payload['attributes'] = {'Key1=Value1', 'LaneCount=2', 'StreetType=Lane'}  (6)

headers = {'TestGuide-AuthKey': authKey}  (7)

uploadFile = {'file': (os.path.basename(file), open(file, 'rb'))}
r = requests.post(u"{0}/api/artifact/artifacts".format(host),
                  params=payload, files=uploadFile, verify=True, headers=headers)

if r.status_code < 300:
    print("Upload successful.")
else:
    print("Upload error: {0} - {1}", r.status_code, r.content)
```

| **1** | Path to the upload file                                     |
|-------|-------------------------------------------------------------|
| **2** | Project ID                                                  |
| **3** | Depository ID into which the file should be uploaded.       |
| **4** | User authentication key                                     |
| **5** | test.guide host URL                                         |
| **6** | Additional important file information for finding the file. |
| **7** | Header containing the authentication information.           |

The finished uploaded artifact in test.guide looks as follows:

## 7.6. Archiving project

In many projects, a large number of reports are collected over the project duration. Not all reports are relevant for delivery and are not required for current developments, but they do take up a lot of database storage space over the years. For this reason, it is advisable <u style="color: blue;">to delete old reports</u> that are no longer required or to export them from the project.

### 7.6.1. Archiving Script

With the following script it is possible to select a specific time range to export all reports in this range to a specified directory of your choice.

The exported reports are stored in a folder structure under `<Year>/<Month>/<Day>/<executionTimestamp>-<reportId>-<testsuiteName>.zip` so that they can be easily imported again, e.g. from a specific month or day.

After successful export, the report is also deleted from test.guide if it is not assigned to a locked release.

- Python script: [TGExportAndArchiveReports.py](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/ArchiveProject/TGExportAndArchiveReports.py)

The following code section shows the parameterization of the script:

``` python
def __WaitUntilDeletionIsFinished(self, taskId: str):
        headers = {
            'Accept': 'application/json',
            'TestGuide-AuthKey': self.__authKey
        }
        endpoint = f"{self.__url}/api/report/reports/deletestatus/{taskId}"
        while True:
            response = requests.get(endpoint, headers=headers,
                                    params=self.__defaultAuthPayLoad,
                                    verify=self.REQUESTS_VERIFY)
            response.raise_for_status()

            jsonResponse = response.json()
            deleteStatus = jsonResponse.get("status")
            msg = jsonResponse.get("detailedMessage")
            if deleteStatus == 'success':
                logging.info(f'\tDeletion of task id {taskId} is finished: {msg}')
                return True
            if deleteStatus == 'error':
                if "test reports belonging to a locked release" in msg:
                    logging.warning(f'\tDeletion task aborted because: {msg}')
                    return True
                else:
                    raise RuntimeError(f'\tDeletion of task id {taskId} failed: {msg}')
            else:
                logging.debug(f'\tDeletion task is not done yet.... {deleteStatus}')
                time.sleep(5)

if __name__ == '__main__':
    # test.guide access parameter
    # Permissions to view and delete reports are required for archiving.
    AUTHKEY = "jRx1le8=.HanQ3VS7ZlqAgq1YI86P_7sS_5t5WxFKfUMyT1trZMQ="  (1)
    URL = "https://localhost:8443"  (2)
    PROJECT_ID = 1   (3)

    # Export Parameter
    ARCHIVE_FOLDER = os.path.dirname(__file__)  (4)
    ARCHIVE_START_DATE = datetime(2023, 1, 1, 0, 0)  (5)
    ARCHIVE_END_DATE = datetime(2024, 3, 31, 0, 0)  (6)
    USE_EXPORT_STORAGE = False  (7)

    ARCHIVAR = TGReportArchivist(URL, AUTHKEY, PROJECT_ID, ARCHIVE_FOLDER, USE_EXPORT_STORAGE)
    ARCHIVAR.StartArchiving(ARCHIVE_START_DATE, ARCHIVE_END_DATE)
```

| **1** | User authentication key with permissions to view and delete reports |
|----|----|
| **2** | test.guide host URL |
| **3** | test.guide project ID |
| **4** | Directory in which the exported reports are to be archived structured by date. The directory in which the script is started is currently used. |
| **5** | Start date from which the reports are exported. |
| **6** | End date up to which day the reports are exported. |
| **7** | True if larger resulting export files are to be expected (\> 1GB). It is then necessary to use the configured export/import storage. |

The finished export looks as follows:

Extract from the log of script

    ### Archive report id 280 ###
    Start export of report id 280
    Export of report id 280 is being processed under task id 9d2814a2-9f6c-4721-8a55-ad9384cf713d.
    Export task 9d2814a2-9f6c-4721-8a55-ad9384cf713d is finished
    Download report c:\...\ArchiveProject\2023\10\27\1698434468.0-280-ProjectD.zip...
    Download report c:\...\ArchiveProject\2023\10\27\1698434468.0-280-ProjectD.zip finished
    Start Deletion of report id 280
    Deletion of report id 280 is being processed under task id 62733baa-d240-4ee0-9aee-9c031188b134.
    Deletion task is not done yet....
    Deletion of task id 62733baa-d240-4ee0-9aee-9c031188b134 is finished: Report was removed successfully: Report ID 280
    #############################
    ### Archive report id 127 ###
    Start export of report id 127
    Export of report id 127 is being processed under task id 4fff1ffc-232f-494a-892d-71356f098924.
    Export task 4fff1ffc-232f-494a-892d-71356f098924 is finished
    Download report c:\...\ArchiveProject\2023\12\12\1702402808.0-127-ProjectB.zip...
    Download report c:\...\ArchiveProject\2023\12\12\1702402808.0-127-ProjectB.zip finished
    Start Deletion of report id 127
    Deletion of report id 127 is being processed under task id 25cbb50e-d49e-4c52-8647-c153c292b626.
    Deletion task aborted because: Could not remove 'TestSuiteExecution(id=127, projectId=1, name=ProjectB, start=2023-12-12T17:38:38Z, atxId=127)' (ATX report AtxId(127)) because it contains test reports belonging to a locked release.
    #############################

Successful archiving then looks like this:

## 7.7. X2Coverage (Just "cover" everything...)

The coverage analysis in **test.guide** is a powerful and highly customizable feature. As the use cases and data sources are different for each customer and project, we recommend using a script to create coverage filter definitions. The script acts as an adaptor between the source of data to cover test case executions against and the coverage filter XML representation that **test.guide** expects. After creating the coverage filter XML, the script may upload the coverage filter definition using **test.guide** 's API.

### 7.7.1. Requirements-Excel2Coverage

In the following you will find an example that creates a *coverage filter definition XML* from a list of *Requirements* that are managed in an Excel file. The script is written in *Python*.

- Requirements Excel example: [Requirements.xlsx](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/X2Coverage/Excel2CoverageExample/Requirements.xlsx)
- Python script: [RequirementsExcelToCoverageDefinition.py](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/X2Coverage/Excel2CoverageExample/RequirementsExcelToCoverageDefinition.py)

The following code section shows the parameterization of the script for testing:

``` python
if __name__ == '__main__':
    rootPath = os.path.dirname(os.path.abspath(__file__))

    # Excel file converter specifications
    INPUT = os.path.join(rootPath, "Requirements.xlsx")  (1)
    OUTPUT = os.path.join(rootPath, "filterTree2.xml")  (2)

    # test.guide upload parameters
    AUTHKEY = "nOPVJ3T6JwqUAR8skQ~yourAuthKey~"  (3)
    URL = "https://your.test-guide.instance:8443"  (4)
    PROJECT_ID = 1  (5)
    FILTER_CATEGORY = "Requirement/Excel"  (6)
    FILTERNAME = "Excel-Export"  (7)
    IS_FILTER_PUBLIC = True  (8)
    FILTER_DESC = "List of all requirements"  (9)

    CON = Converter(INPUT, OUTPUT)
    if CON.CreateFilterTree():
        UPLOADER = TGUploader(URL, AUTHKEY, PROJECT_ID)
        UPLOADER.UploadXmlConfig(OUTPUT, FILTERNAME, FILTER_CATEGORY,
                                 IS_FILTER_PUBLIC, FILTER_DESC, True)
```

| **1** | Path to the requirements Excel example file |
|----|----|
| **2** | Path of the coverage filter definition output file |
| **3** | User authentication key |
| **4** | test.guide host URL |
| **5** | Project ID |
| **6** | Optional category of the coverage filter. |
| **7** | Coverage filter name |
| **8** | True, if the coverage should be public usable for everyone in the project, otherwise False. |
| **9** | Optional description for coverage |

The finished coverage in test.guide looks as follows:

## 7.8. Report Management API

The Report Management API allows access to test reports and test case executions.

### 7.8.1. Exporting the test case executions of a release to an Excel sheet

[This Python example script](https://testguide.one-cx.cn/help-docs/070_Developing/files/python/ReportManagementAPI/Export/TGReleaseExport.py) illustrates how the Release API and the Report Management API can be used together to export the contents of a release (that is, the test case executions it contains) to an Excel file.

The following excerpt from the script shows how to use it:

``` python
# pylint: disable=missing-docstring,invalid-name

class TGReleaseExport(object):

    REQUESTS_VERIFY = True

    def __init__(self, url, authKey): (1)
        '''
        Constructor.
        @param url: URL of test.guide instance
        @type url: unicode
        @param authKey: authentication key for accessing API
        @type authKey: unicode
        '''
        self.apiUrl = url + '/api/'
        self.authKey = authKey

    def exportReleaseAsExcel(self, releaseId, projectId, targetFile): (2)
        '''
        Export the release as XLSX file.
        @param releaseId: ID of the release
        @type releaseId: int
        @param projectId: ID of the project the release belongs to
        @type projectId: int
        @param targetFile: Path to target Excel file.
        '''
        tagSetId = self._getTagSetId(releaseId)
        taskId = self._startExport(tagSetId, projectId)
```

| **1** | Create a new TGReleaseExport object by calling the constructor and supplying the URL of the test.guide host and the authentication key of a user (preferably a technical user). |
|----|----|
| **2** | Calling this method starts the export, waits for the export to finish and finally downloads the Excel file. To use it, supply a release ID, a matching project ID as well as the path of the target Excel file. |

This can be done, for example, as follows:

``` python
from TGReleaseExport import TGReleaseExport

url = u"https://localhost:8443"
authKey = u"bkN0ZGtpdFA0bz..."

releaseId = 112
projectId = 2
targetFile = "myExcelFile.xlsx"

exporter = TGReleaseExport(url, authKey)
exporter.exportReleaseAsExcel(releaseId, projectId, targetFile)
```

## 8 Troubleshooting

## 8.1. Working with logs

**Acquiring the log files for** **test.guide**

- Via **test.guide**: <u style="color: blue;">**General**</u> → Download Logfiles
- Via the file system of the host that runs **test.guide**: `~TG_WORKSPACE~\TTS-TM\logs`

You can set the logging level for troubleshooting at <u style="color: blue;">**General**</u>.info

| Log file | Description |
|----|----|
| ops.log | Main log for operating **test.guide**, contains the internal logs depending on the log level plus logs of external frameworks and libraries on log level ERROR |
| debug.log | Log for debugging **test.guide** (intended mainly for developers), contains the internal logs depending on the log level |
| thirdparty.log | Logs from external frameworks and libraries |
| systeminfo.log | Contains general system information, e.g. which **test.guide** version is used, PostgreSQL configuration, ... |
| performance.log | Contains the performance logs that log critical parts of the application |
| db-migration.log | Logs from Liquibase and custom changes, useful for debugging problems while migrating the database |
| admin.log | Logs of relevant configuration changes in **test.guide**, e.g. deleting users |
| api-access.csv | Log of all REST API accesses to **test.guide** |
| usage.log | Contains the usage statistics as shown on the Usage statistics page. They are particularly useful for the operator to analyze which features are used and to size the system accordingly for the relevant use. |

In addition, there may be other log files, e.g. to log special frameworks (EclipseLink, BIRT) separately or to create dedicated logs with a longer retention period for troubleshooting.

**Acquiring the log files for the** **ResourceAdapter**

You can set the logging level for troubleshooting in the <u style="color: blue;">**ResourceAdapter** configuration</u>.info

## 9 FAQs

Frequently asked questions and other interesting topics about test.guide and its connection to ecu.test can be found in the [tracetronic Knowledge Base](https://kbtracetronic.atlassian.net/wiki/spaces/KB/overview).

## 10 Glossary

The following glossary explains technical and professional terms that are used in the documentation.

Automotive Test Exchange Format (ATX)

ATX was created by the Association for Standardization of [Automation and Measuring Systems (ASAM)](https://www.asam.net/) as a standard for the uniform exchange of tests in the automotive area.

Issue Tracker

**test.guide** can interact with certain third party tools that can be summarized as <u style="color: blue;">"Issue Trackers"</u>. From a **test.guide** user perspective, these are tools for managing bug or defect tickets. Interaction with these tickets is possible in different ways as described <u style="color: blue;">here</u> or <u style="color: blue;">here</u>.

Management Tool / Test Management Tool

**test.guide** can interact with certain third party tools that can be summarized as <u style="color: blue;">"Test Management Tools"</u>. These tools are typically used to manage test designs, as well as final test results. Many of those tools also span the entire life cycle of a product and are also referred to as ALM Application Lifecycle Management Tools. As such, they are also often used to manage requirements as well as tickets such as bug tickets and defect tickets.**test.guide** can interact with these tools in different ways as described <u style="color: blue;">here</u>.

ecu.test package

A package in **ecu.test** is a XML-based file, that can contain both, a test case or just a library function used within a test case.

ResourceAdapter (RA)

A java-based client application that is used as a sensor and agent for connecting <u style="color: blue;">**test resource machine**</u> s to **test.guide**. This application comes with **test.guide**.

Test bench

A <u style="color: blue;">**test resource**</u> that can be used for executing (automated) test cases (e.g. hardware-in-the-loop test bench (HiL)).

Test infrastructure

Entirety of all <u style="color: blue;">**test resource**</u> s available for testing purposes. A module in **test.guide** for managing all the <u style="color: blue;">**test resource**</u> s is named like this.

Test resource (TR)

Generic term for a technical device used to perform tests or parts of tests like analysis (e.g. a <u style="color: blue;">**test bench**</u>, a <u style="color: blue;">**workstation**</u>, a virtual (SiL) <u style="color: blue;">**test bench**</u> in the cloud, ...).

Test resource machine (TRM)

A test resource machine is always a child element of a <u style="color: blue;">**test resource**</u> and means a system on which a **ResourceAdapter** can be executed (e.g. a control PC of a HiL <u style="color: blue;">**test bench**</u>).

TRM activity

Activity of a <u style="color: blue;">**test resource machine**</u> that can be reported by various plug-ins. Describes what is currently happening on the <u style="color: blue;">**test resource machine**</u>.

TRM state

Aggregation of all status information for a <u style="color: blue;">**test resource machine**</u>, which is made up of connection state, monitoring state and component state. Describes the condition or health of the <u style="color: blue;">**test resource machine**</u>.

TRF report

TRF is the file extension of a test report generated by **ecu.test**. This is a proprietary format that can only be opened with **ecu.test** or the report viewer it contains.

Workstation

A <u style="color: blue;">**test resource**</u> on which analysis or other CPU-intensive pre- or post-processing for tests can be carried out that do not necessarily have to run on a <u style="color: blue;">**test bench**</u>.

x2atx (X2ATX)

A plug-in framework within **test.guide** to import report data from other formats than <u style="color: blue;">**ATX**</u>.

X-in-the-loop (XiL)

A X-in-the-loop <u style="color: blue;">**test bench**</u> means any kind of a closed-loop <u style="color: blue;">**test bench**</u>. The "X" can be replaced by "H" for hardware, "S" for software, "M" for model, "P" for processor or "V" for vehicle.

*Something is missing? More documentation is coming soon!*

##**Maven Essentials**##

**Step By Step installation of Maven:**
- Install java first: 
  - apt install oracle-java12-installer
- downlaod and install maven:
- install under root /opt
  - wget <maven dowload-link> -O maven
  - tar -xvzf maven
- cd to Maven directory
  - check files with ll or ls
  - cd /etc/profile.d/ ~ to check files
  - cat jdk.sh 
  - echo the save to profile like so 
    - echo "export PATH=$PATH:/opt/maven/bin/" >> maven.sh
    - echo "export MVN_HOME=/opt/maven" >> maven.sh
    - chmod +x  maven.sh
  - source /etc/profile.d/maven.sh
  - now you can run:  mvn -version  

**Maven Repository:** 
- a place to downlaod dependencies which can be from:
    - local repo   ~ your machine
    - remote repo ~ company/group
    - central repo ~ maven community repo

**Basics:**
- POM (project object model) 
  ~ a list of dependencies which can be dowloaded or referred (locally or central repos) 
- build lifecycles
  ~ each phase refers to a specific task
- build profiles  cofigs for a build process (configs & values).  These are usaully set in the POM file
- build plugins ~ a group of goals  for a specific task. plugins can be downloaded from maven repo

**Architecture:**
- one deployed, reads pom.xml, from which it gets dependencies, plugines profiles and goals, which it gathers to make the build possible.
- creates a report of reqs, lifecycles etc.

**Maven build lifecycle:**
3 main steps - 
defualt - haldles project deployment 
clean - handles project clearning
site - handles project site documentation
  - Build lifecyle phases:  copile, test-complile, test, package, integration-test, verify, install, deploy

**Advantages of Maven:**
- manages all processes of the build, 
   - building, documentation, releasing, distribution and project mgmt
- simplifyes the process  and increaese performance
- dependencies are collected automatically
- easy access to required info
- independent of platform or os
- easy adding of dependencies
- supports integration with other tools

**Interview Questions:**
What is maven: an opensource build tool used to build, publish, deploy several projects at once
written in java but canl build projects written in C#, Scala, Ruby, and Java, and integrated with Eclipse
what does it help with: heps with building, documentation, releasing, distribution and prject mgmet. It can identify listed dependencies 
and fetch those to complete build
what elements does maven take care of: takes care of builds, dependencies, reports, distribution, releases, and mailing list

**Differences between ANT and Maven:**
- maven has conventions in pom.xml, while ANT does no formal convention its info can be provided with build.xml file
- maven is declarative, while ant is procedureal
- maven has a lifecycle, whilst ant doesnt
- maven can be used as a pm took, whilst ant does not support that
- maven plugins are reusasble, whilst not so in ANT. 
- Ant is specifically a build tool 

**What is POM:**
~ a pom file is an xml file with info regrading the projectand config details. 
it contains description of project, info about versioning and config mgmt for the project
it is usually on the home directory which contains mainly configs  about dependencies, developers & contribs, plugins, plugin configs & resources.
Minimum reqs for a POM file: min regs elements are; 
  - project root, 
  - modelVersion ~ which shuold be 4.0.0
  - groupId ~ project group id
  - artifactId ~ artificat id
  - Version ~ version of the artifact

**what is meatnt by a build tool:**
~ is essentially, the process of turning code into a artifact pusuant of the following:
- generating code
- generating documentation
- compiling source code
- packaging of compiles jar files
- installing packages to repos 

**steps to  install Maven on Windows:**
- download maven & extract
- set environment variables JAVA_HOME and MAVEN_HOME
- add environment variables
- lastly verify installation is completed.

**Gotchas:**
- to run commands you dont type the full name but "mvn"
- sometimes your java envvar might be pointing to the wrong path
- settings can be changed, which can be fixed by looking at the settings file
- the repos in a hidden file 
- maven operates on port 8080
- maven port can be changed by updating tomcat server.port=8181




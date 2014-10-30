mobileuiautomation
==================

# Setup Appium

To setup appium and start appium, follow readme in https://github.com/sangeethasriniv/framework

# Clone this test repo
git clone https://github.com/sangeethasriniv/sampleuitests.git

# Init Submodules  (to get the framework submodule)
```
git submodule init
git submodule update
```

# Setup Eclipse 
Install Eclipse
Install Pydev (Eclipse -> Help -> Install New Software -> Add-> (Name: pydev, url : http://pydev.org/updates) , choose pydev in table below and click install

# Import project to eclipse
Open eclipse
File->import->git->projects from git -> existing local repo -> add the folder path of the cloned repo -> import existing projects

# Run tests in eclipse
Project->Run->Runconfigurations->Python unit tests-> ios-test -> click run

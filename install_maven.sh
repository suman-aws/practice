#!/bin/bash

# Specify the Maven version to install
MAVEN_VERSION=3.8.1

# Directory where Maven will be installed
INSTALL_DIR=/opt

# Download URL for the specified Maven version
MAVEN_URL=https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz

# Installation path
MAVEN_HOME=$INSTALL_DIR/apache-maven-$MAVEN_VERSION

# Check if Maven is already installed
if [ -d "$MAVEN_HOME" ]; then
  echo "Maven $MAVEN_VERSION is already installed at $MAVEN_HOME"
  exit 0
fi

# Download Maven
echo "Downloading Maven $MAVEN_VERSION..."
wget $MAVEN_URL -P /tmp

# Extract the downloaded tar file
echo "Extracting Maven..."
tar -xzvf /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz -C $INSTALL_DIR

# Clean up the downloaded tar file
rm /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz

# Set up environment variables
echo "Setting up environment variables..."
PROFILE_FILE=~/.bashrc  # Change this to ~/.zshrc if you are using zsh

# Check if the environment variables are already set
if ! grep -q "export M2_HOME=$MAVEN_HOME" "$PROFILE_FILE"; then
  echo "export M2_HOME=$MAVEN_HOME" >> $PROFILE_FILE
fi

if ! grep -q 'export PATH=$M2_HOME/bin:$PATH' "$PROFILE_FILE"; then
  echo 'export PATH=$M2_HOME/bin:$PATH' >> $PROFILE_FILE
fi

# Source the profile file to apply changes
echo "Applying environment variables..."
source $PROFILE_FILE

# Verify Maven installation
echo "Verifying Maven installation..."
mvn -version

echo "Maven $MAVEN_VERSION installation completed successfully."

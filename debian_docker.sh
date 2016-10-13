# Preliminaries - not always in default docker container
apt-get update
apt-get install -y sudo

sudo apt-get update
sudo apt-get install -y git python3-dev python3-tk
sudo apt-get install -y git

python3 --version

sudo apt-get install -y wget

wget https://github.com/atom/atom/releases/download/v1.9.9/atom-amd64.deb

# This command will error with unmet dependencies
sudo dpkg --install atom-amd64.deb
# Fix the dependencies with this command
sudo apt-get -f install -y

# Install Hydrogen plugin
sudo apt-get install -y build-essential libzmq3-dev
PYTHON=python2.7 apm install hydrogen

cat >> ~/.bashrc << EOF

# Put the path to the local bin directory into a variable
py3_local_bin=\$(python3 -c 'import site; print(site.USER_BASE + "/bin")')
# Put the directory at the front of the system PATH
export PATH="\$py3_local_bin:$PATH"
EOF

source ~/.bashrc

echo $PATH

# Download the get-pip.py installer
wget https://bootstrap.pypa.io/get-pip.py
# Execute the installer for Python 3 and a user install
python3 get-pip.py --user

which pip3

pip3 install --user numpy scipy matplotlib ipython nibabel jupyter

wget https://bic-berkeley.github.io/psych-214-fall-2016/_downloads/check_install.py

python3 check_install.py

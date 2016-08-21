# Preliminaries - not in default docker container
dnf install -y sudo which

sudo dnf install -y python3-devel git

python3 --version

sudo dnf install -y wget

wget https://github.com/atom/atom/releases/download/v1.9.9/atom.x86_64.rpm

sudo dnf install -y ./atom.x86_64.rpm

# Install dependencies for hydrogen plugin build
sudo dnf install -y python2 gcc-c++ zeromq3-devel
# Install hydrogen plugin
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

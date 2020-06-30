#! /bin/bash
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`
current_dir=$PWD

echo "${green}Preparing Virtual Environment...${reset}"
virtualenv ../venv
source ../venv/bin/activate


echo "${green}Installing python dependencies...${reset}"
echo "Please select your environment"
select choice in "mac" "linux"; do
    case $choice in
        linux ) pip install gdal==2.2.4; break;;
        mac ) pip install gdal==2.3.1; break;;
    esac
done
pip install -r requirements.txt


echo "${green}Preparing django app...${reset}"
echo "Please write your project name:"
read varname
cd ../
django-admin startproject project
mv project $varname
cp $current_dir/settings.py $varname/project/settings.py
cp $current_dir/local_settings.py $varname/project/local_settings.py
cp $current_dir/urls.py $varname/project/urls.py
cp $current_dir/project_readme.md $varname/readme.md
cp $current_dir/requirements.txt $varname/requirements.txt
cp $current_dir/.gitignore $varname/.gitignore

echo "${green}Preaparing directory...${reset}"
cd $varname
mkdir apps
mkdir upload
mkdir static
cat <<EOF >apps/__init__.py
EOF


echo "${green}Initializing git...${reset}"
git init
cd project
cat <<EOF >.gitignore
local_settings.py
EOF
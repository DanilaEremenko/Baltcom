#! /bin/bash
die() {
  printf "ERROR:$*\n" 1>&2
  exit 1
}

cfg_file="../config_files/db_config.json"

if [[ -f $cfg_file ]]; then
  cfg_text=$(cat $cfg_file)
  db_name=$(printf "$cfg_text" | grep 'NAME' | cut -d ':' -f2 | sed -e 's/,//' -e 's/\"//g' -e 's/ //g')
  db_user=$(printf "$cfg_text" | grep 'USER' | cut -d ':' -f2 | sed -e 's/,//' -e 's/\"//g' -e 's/ //g')
  db_password=$(printf "$cfg_text" | grep 'PASSWORD' | cut -d ':' -f2 | sed -e 's/,//' -e 's/\"//g' -e 's/ //g')
else
  die "no $cfg_file file"
fi

printf "db_name = $db_name\n db_user = $db_user \n db_password = $db_password\n"

psql \
  -c "create database $db_name;" \
  -c "create user $db_user with password '$db_password';" \
  -c "grant all privileges on database $db_name to $db_user;"

#psql \
#psql -d $db_name -c "grant all on session to $db_user;"
#psql -d $db_name -c "grant all on news to $db_user;"
#psql -d $db_name -c "grant all on stories to $db_user;"

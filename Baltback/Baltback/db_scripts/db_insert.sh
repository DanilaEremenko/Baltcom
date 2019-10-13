#!/bin/bash

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
  -d $db_name -c "insert into articles_article values (0,'article_1','text_1','now');" \
  -d $db_name -c "insert into articles_article values (1,'article_2','text_2','now');"

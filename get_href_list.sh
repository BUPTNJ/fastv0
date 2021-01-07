file_name="city.html"
wget http://ip.bczs.net/city -O $file_name
./format.sh $file_name
cat $file_name | gawk -f parse_href 
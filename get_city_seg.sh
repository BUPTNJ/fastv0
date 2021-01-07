city_name=$1
echo "extracting href...">&2
href=`cat href_list | grep $city_name |gawk '{print $2}'`
file_name="$city_name.html"
wget $href -O $file_name
echo "formatting html file...">&2
./format.sh $file_name
cat $file_name |gawk -f parse_seg
echo "done!">&2
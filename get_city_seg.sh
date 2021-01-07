city_name=$1
echo "extracting href..."
href=`cat href_list | grep $city_name |gawk '{print $2}'`
file_name="$city_name.html"
wget $href -O $file_name
echo "formatting html file..."
./format.sh $file_name
cat $file_name |gawk -f parse_seg
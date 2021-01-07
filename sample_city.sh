#judge if city_seg exist
file_name="$1_seg"
if [ ! -e $file_name ]; then
    ./get_city_seg.sh $1 > $file_name
fi
cat $file_name | gawk -f sample_target
./sample_city.sh $1 > $1_sample
scamper -f $1_sample > $2_trace_$1

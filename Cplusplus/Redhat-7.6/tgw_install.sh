IS_UBUNTU=`cat /proc/version | grep Ubuntu`
IS_REDHAT=`cat /proc/version | grep "Red Hat"`
CRT_PATH="$HOME/mdga_file"
LIB_PATH="$CRT_PATH/lib"
IS_SET_TGW=`cat $HOME/.bash_profile | grep "mdga_file/lib"`
ENV_SET_FILE="$HOME/.bash_profile"

Date()
{
    d=`date +"%Y-%m-%d %H:%M:%S"`
    echo "$d"
}
if [ -n "$IS_REDHAT" ]; then
    echo "$(Date)"
    source $ENV_SET_FILE
    if [ ! -n "$IS_SET_TGW" ]; then
    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LIB_PATH" >> $ENV_SET_FILE
    fi
    if [ ! -d $CRT_PATH ]; then
    mkdir $CRT_PATH
    else
    rm $CRT_PATH/.ca.crt
    fi
    if [ ! -d $LIB_PATH ]; then
    mkdir $LIB_PATH
    else
    rm $LIB_PATH/* -f
    fi
    cp $PWD/c++/lib/.ca.crt $CRT_PATH
    cp -rf $PWD/c++/lib/* $LIB_PATH
    source $ENV_SET_FILE
else
echo "only support ReadHat"
fi

git submodule update --init --recursive

cd base || exit 1

excluded_dirs="base workshop-setup"
directories=$(ls -d ../*/ | grep -vE "($(echo $excluded_dirs | sed 's/ /|/g'))/")

# For each directory I need to do the following:
# hugo --minify --config {DIRECTORY_PATH}/config.toml --contentDir {DIRECTORY_PATH}/content/ --destination ../public/{DIRECTORY_NAME}
# Note: In the DIRECTORY_NAME part, I need to strip any relative path info and just get the actual directory name
for dir in $directories; do
	dir_name=$(basename $dir)
	hugo --minify --config "${dir}/config.toml" --contentDir "${dir}/content/" --destination "../public/${dir_name}" --baseURL="/cloudbees-field-workshops/${dir_name}/"
done

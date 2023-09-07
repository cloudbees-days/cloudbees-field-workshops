git submodule update --init --recursive

cd base || exit 1

excluded_dirs="base workshop-setup public"
directories=$(ls -d ../*/ | grep -vE "($(echo $excluded_dirs | sed 's/ /|/g'))/")

echo "<html><head><title>CloudBees Labs</title></head><body>" >../public/index.html
echo "<h1>Current Labs</h1><ul>" >>../public/index.html

for dir in $directories; do
	dir_name=$(basename $dir)
	hugo --minify --config "${dir}/config.toml" --contentDir "${dir}/content/" --destination "../public/${dir_name}" --baseURL="/cloudbees-field-workshops/${dir_name}/"

	echo "<li><a href=\"/cloudbees-field-workshops/${dir_name}/\">${dir_name}</a></li>" >>../public/index.html
done

echo "</ul></body></html>" >>../public/index.html

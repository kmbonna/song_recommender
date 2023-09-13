mkdir -p ~/.streamlit/
cp config.toml ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
" > ~/.streamlit/config.toml
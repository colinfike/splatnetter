mkdir build
cp splatnetter.py build/
pip install -r requirements.txt -t build/
cd build && zip -r ../splatnetter.zip .

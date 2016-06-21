echo "Welcome to Grove Indoor Environment Kit Hackathon"

cat << EOM > /etc/opkg/base-feeds.conf
src/gz all http://repo.opkg.net/edison/repo/all
src/gz edison http://repo.opkg.net/edison/repo/edison
src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32
EOM

opkg update

git clone https://github.com/xe1gyq/GiekHackathon.git
cd GiekHackathon/
pip install pip --upgrade

echo
echo "Now go to GiekHackathon directory to get started!"
echo
echo "Happy GiekHackathon'ing"

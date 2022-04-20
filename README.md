# dotfiles
linux config file

rm -rf ~/.config/i3
sudo ln -s ~/Documents/github/dotfiles/.config/i3 ~/.config/i3

rm -rf ~/.config/i3status
sudo ln -s ~/Documents/github/dotfiles/.config/i3status ~/.config/i3status

rm -rf ~/.config/ranger
sudo ln -s ~/Documents/github/dotfiles/.config/ranger ~/.config/ranger

rm -rf ~/.config/picom
sudo ln -s ~/Documents/github/dotfiles/.config/picom ~/.config/picom

rm -rf ~/.config/kitty
sudo ln -s ~/Documents/github/dotfiles/.config/kitty ~/.config/kitty

rm -rf ~/.config/qutebrowser
sudo ln -s ~/Documents/github/dotfiles/.config/qutebrowser ~/.config/qutebrowser

rm -rf ~/.config/fish
sudo ln -s ~/Documents/github/dotfiles/.config/fish ~/.config/fish

sudo ln -s ~/Documents/github/dotfiles/.config/nvim ~/.config/nvim
sudo ln -s ~/Documents/github/dotfiles/.bash_aliases ~/.bash_aliases
sudo ln -s /home/xyz/Documents/deb-installer/Obsidian-0.13.31.AppImage /usr/bin/obsidian
sudo ln -s /home/xyz/Documents/deb-installer/ksnip-1.9.2-x86_64.AppImage /usr/bin/ksnip

sudo cp /home/xyz/Documents/deb-installer/dmenu_run_history /usr/bin/


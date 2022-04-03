# dotfiles
linux config file

rm -rf ~/.config/i3
rm -rf ~/.config/ranger

sudo ln -s ~/Documents/github/dotfiles/.config/ranger ~/.config/ranger
sudo ln -s ~/Documents/github/dotfiles/.config/nvim ~/.config/nvim
sudo ln -s ~/Documents/github/dotfiles/.config/i3 ~/.config/i3
sudo ln -s ~/Documents/github/dotfiles/.config/i3status ~/.config/i3status
sudo ln -s ~/Documents/github/dotfiles/.config/picom ~/.config/picom
sudo ln -s ~/Documents/github/dotfiles/.config/qutebrowser ~/.config/qutebrowser
sudo ln -s ~/Documents/github/dotfiles/qutebrowser /usr/local/bin/qutebrowser
sudo ln -s ~/Documents/github/dotfiles/.local/share/qutebrowser /home/xyz/.local/share/qutebrowser
sudo ln -s ~/Documents/github/dotfiles/.bash_aliases ~/.bash_aliases

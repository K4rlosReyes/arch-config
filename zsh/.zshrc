export PATH="$HOME/.emacs.d/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"
export TMPDIR='/var/tmp'
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v

source "${HOME}/.zgenom/zgenom.zsh"
# Check for plugin and zgenom updates every 7 days
# This does not increase the startup time.
zgenom autoupdate

if ! zgenom saved; then
  echo "Initializing zgenom"

  # NOTE Be extra careful about plugin load order, or subtle breakage can
  #   emerge. This is the best order I've sussed out for these plugins.
  zgenom load spaceship-prompt/spaceship-prompt
  zgenom load zdharma-continuum/fast-syntax-highlighting
  zgenom load zsh-users/zsh-completions src
  zgenom load zsh-users/zsh-autosuggestions
  zgenom load zsh-users/zsh-history-substring-search

  zgenom save
  zgenom compile "$HOME/.zshrc"
fi

alias ml="source ~/.ml38/bin/activate"
alias work="cd ~/Work"
alias comm="ml && python ~/Work/python-comm/comm.py"

alias wf="nmcli connection up KR7X --ask"
alias wc="windscribe connect"
alias wd="windscribe disconnect"

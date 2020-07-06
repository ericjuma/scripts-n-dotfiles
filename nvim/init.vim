if empty(glob('~/.local/share/nvim/site/autoload/plug.vim'))
  silent !curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()
" Plug 'vim-python/python-syntax'
Plug 'kien/ctrlp.vim'
Plug 'tpope/vim-repeat'
Plug 'junegunn/goyo.vim'
Plug 'takac/vim-hardtime'
Plug 'tpope/vim-surround'
Plug 'ap/vim-css-color'
Plug 'justinmk/vim-sneak'
Plug 'jceb/vim-orgmode'
Plug 'dylanaraps/wal.vim'
Plug 'terryma/vim-smooth-scroll'
call plug#end()

set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set wildmenu
set sidescrolloff=1
set nowrap
set scrolloff=4
syntax on
filetype plugin indent on
let mapleader="\<Space>"
let maplocalleader="//"
set mouse=a
colorscheme wal
" let g:zenmode_colorscheme = "wal"
" let g:ctrlp_working_path_mode = 'ra'
" let g:ctrlp_root_markers = ['.config']
" let g:ctrlp_show_hidden = 1
let g:ctrlp_prompt_mappings = {
\ 'PrtSelectMove("j")':   ['<down>'],
\ 'AcceptSelection("r")': ['<c-j>'],
\ }
let g:ctrlp_cache_dir = $HOME . '/.cache/ctrlp'
if executable('rg')
  let g:ctrlp_user_command = 'rg %s --hidden --files --color=never --glob "!.git"'
  let g:ctrlp_use_caching = 0
endif
nnoremap <c-p> :CtrlPMRU<CR>
let g:ctrlp_map = '<c-n>'
let g:ctrlp_cmd = 'CtrlP'

nnoremap <C-_> :Goyo <CR>i<ESC>
nnoremap <c-s> :w<CR>
nnoremap <leader>ev :edit $MYVIMRC<CR>
nnoremap <leader>sv :source $MYVIMRC<CR>
nnoremap <leader>sw2 :set shiftwidth=2<CR>
nnoremap <leader>sw3 :set shiftwidth=3<CR>
nnoremap <leader>sw4 :set shiftwidth=4<CR>
if has ('autocmd') " Remain compatible with earlier versions
 augroup vimrc     " Source vim configuration upon save
    autocmd! BufWritePost $MYVIMRC source % | echom "Reloaded " . $MYVIMRC | redraw
    autocmd! BufWritePost $MYGVIMRC if has('gui_running') | so % | echom "Reloaded " . $MYGVIMRC | endif | redraw
  augroup END
endif " has autocmd
autocmd Filetype html setlocal ts=2 sw=2 expandtab
autocmd Filetype ruby setlocal ts=2 sw=2 expandtab
set foldnestmax=2
set foldmethod=indent
set foldlevel=2
set smartcase

tnoremap <esc>m <C-\><C-n><c-o>
nnoremap <esc>m :term<cr>

" let g:python_highlight_all = 1
set clipboard=unnamedplus
nnoremap <leader><Space> :nohlsearch<CR>
nnoremap <leader>cp ggyG

noremap <silent> <c-u> :call smooth_scroll#up(&scroll, 20, 2)<CR>
noremap <silent> <c-d> :call smooth_scroll#down(&scroll, 20, 2)<CR>
noremap <silent> <c-b> :call smooth_scroll#up(&scroll*2, 20, 4)<CR>
noremap <silent> <c-f> :call smooth_scroll#down(&scroll*2, 20, 4)<CR>

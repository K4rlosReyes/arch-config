;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;; Some functionality uses this to identify you, e.g. GPG configuration, email
;; clients, file templates and snippets. It is optional.
(setq user-full-name "Carlos Reyes"
      user-mail-address "carlosreyesml18@gmail.com")

(setq! evil-vsplit-window-right t
      evil-split-window-below t)

(defadvice! prompt-for-buffer (&rest _)
  :after '(evil-window-split evil-window-vsplit)
  (consult-dir))

(add-hook! 'python-mode-hook
           (pyvenv-activate "~/.ml38"))
(add-hook! 'python-mode-hook #'tree-sitter-hl-mode)
(setq-hook! 'python-mode-hook +format-with-lsp nil)

(after! company
  (setq company-idle-delay nil))
;; Doom exposes five (optional) variables for controlling fonts in Doom:
;;
;; - `doom-font' -- the primary font to use
;; - `doom-variable-pitch-font' -- a non-monospace font (where applicable)
;; - `doom-big-font' -- used for `doom-big-font-mode'; use this for
;;   presentations or streaming.
;; - `doom-unicode-font' -- for unicode glyphs
;; - `doom-serif-font' -- for the `fixed-pitch-serif' face
;;
;; See 'C-h v doom-font' for documentation and more examples of what they
;; accept. For example:
;;
;;(setq doom-font (font-spec :family "Fira Code" :size 12 :weight 'semi-light)
;;      doom-variable-pitch-font (font-spec :family "Fira Sans" :size 13))
;;
(setq doom-font (font-spec :family "mononoki Nerd Font Mono" :size 14 :weight 'regular)
      doom-variable-pitch-font (font-spec :family "mononoki Nerd Font" :size 16))
;; If you or Emacs can't find your font, use 'M-x describe-font' to look them
;; up, `M-x eval-region' to execute elisp code, and 'M-x doom/reload-font' to
;; refresh your font settings. If Emacs still can't find your font, it likely
;; wasn't installed correctly. Font issues are rarely Doom issues!

;; There are two ways to load a theme. Both assume the theme is installed and
;; available. You can either set `doom-theme' or manually load a theme with the
;; `load-theme' function. This is the default:
(setq doom-theme 'doom-one)
(setq default-frame-alist '((undecorated . t)))
(scroll-bar-mode -1)
;; This determines the style of line numbers in effect. If set to `nil', line
;; numbers are disabled. For relative line numbers, set this to `relative'.
(setq display-line-numbers-type nil)

;; If you use `org' and don't want your org files in the default location below,
;; change `org-directory'. It must be set before org loads!
(setq org-directory "~/Notes/org/")

;;; Keybins

;; (map! :leader
;;       (:prefix "n"
;;        "b" #'org-roam-buffer-toggle
;;        "d" #'org-roam-dailies-goto-today
;;        "D" #'org-roam-dailies-goto-date
;;        "i" #'org-roam-node-insert
;;        "r" #'org-roam-node-find
;;        "R" #'org-roam-capture))

(advice-add #'doom-modeline-segment--modals :override #'ignore)

;;; :tools lsp
;; Disable invasive lsp-mode features
(after! lsp-mode
  (setq lsp-enable-symbol-highlighting nil
        ;; If an LSP server isn't present when I start a prog-mode buffer, you
        ;; don't need to tell me. I know. On some machines I don't care to have
        ;; a whole development environment for some ecosystems.
        lsp-enable-suggest-server-download t))
(after! lsp-ui
  (setq lsp-ui-sideline-enable nil  ; no more useful than flycheck
        lsp-ui-doc-enable nil))     ; redundant with K

;;; ORG
(setq +org-roam-auto-backlinks-buffer t
      org-directory "~/Notes/"
      org-roam-directory org-directory
      org-roam-db-location (concat org-directory ".org-roam.db")
      org-roam-dailies-directory "journal/"
      org-archive-location (concat org-directory "org/%s::")
      org-agenda-files org-directory)

(after! org-roam
  (setq org-roam-capture-templates
        `(("n" "note" plain
           ,(format "#+title:: ${title}\n%%[%s/template/note.org]" org-roam-directory)
           :target (file "note/%<%Y%m%d%H%M%S>-${slug}.org")
           :unnarrowed t)
          ("g" "gtd" plain
           ,(format "#+title: ${title}\n%%[%s/template/gtd.org]" org-roam-directory)
           :target (file "gtd/%<%Y%m%d>-${slug}.org")
           :unnarrowed t)
          ("w" "work" plain
           ,(format "#+title: ${title}\n%%[%s/template/work.org]" org-roam-directory)
           :target (file "work/%<%Y%m%d>-${slug}.org")
           :unnarrowed t))
        org-roam-dailies-capture-templates
        '(("d" "default" entry "* %?"
           :target (file+head "%<%Y-%m-%d>.org" "#+title: %<%B %d, %Y>\n\n")))))

(after! org-roam
  (add-to-list 'org-roam-completion-functions #'org-roam-complete-tag-at-point)
  (add-hook 'org-roam-find-file-hook #'org-roam-update-slug-on-save-h)
  (add-hook 'org-roam-buffer-postrender-functions #'magit-section-show-level-2)
  (advice-add #'org-roam-backlinks-section :override #'org-roam-grouped-backlinks-section)
  (advice-add #'org-roam-node-visit :around #'+popup-save-a)
  ;;(advice-add #'org-roam-node-list :filter-return #'org-roam-restore-insertion-order-for-tags-a)
  (advice-add #'org-roam-buffer-set-header-line-format :after #'org-roam-add-preamble-a))

(remove-hook '+doom-dashboard-functions #'doom-dashboard-widget-shortmenu)

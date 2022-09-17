;;; $DOOMDIR/config.el -*- lexical-binding: t; -*-

;;; EXTRA
(setq user-full-name "KR7X"
      user-mail-address "carlosreyesml18@gmail.com")

(setq! evil-vsplit-window-right t
      evil-split-window-below t)

(defadvice! prompt-for-buffer (&rest _)
  :after '(evil-window-split evil-window-vsplit)
  (consult-dir))

(add-hook! 'python-mode-hook
           (pyvenv-activate "~/.ml38"))
(setq-hook! 'python-mode-hook +format-with-lsp nil)

(setq doom-font (font-spec :family "mononoki Nerd Font Mono" :size 14 :weight 'regular)
      doom-variable-pitch-font (font-spec :family "mononoki Nerd Font" :size 16))
(setq doom-theme 'doom-one)
(setq default-frame-alist '((undecorated . t)))
(scroll-bar-mode -1)
(setq display-line-numbers-type nil)


;;; KEYS

(map! :leader
      (:prefix "n"
       "b" #'org-roam-buffer-toggle
       "d" #'org-roam-dailies-goto-today
       "D" #'org-roam-dailies-goto-date
       "i" #'org-roam-node-insert
       "r" #'org-roam-node-find
       "R" #'org-roam-capture))

(advice-add #'doom-modeline-segment--modals :override #'ignore)

;;; LSP CONFIG
(after! lsp-mode
  (setq lsp-enable-symbol-highlighting nil
        lsp-enable-suggest-server-download t))
(after! lsp-ui
  (setq lsp-ui-sideline-enable nil
        lsp-ui-doc-enable nil))

;;; ORG ROAM CONFIG
(setq +org-roam-auto-backlinks-buffer nil
      org-directory "~/Notes/"
      org-roam-directory org-directory
      org-roam-db-location (concat org-directory ".org-roam.db")
      org-roam-dailies-directory "journal/"
      org-archive-location (concat org-directory ".org/%s::")
      org-agenda-files '("~/Notes/"))

(after! org-roam
  (setq org-roam-capture-templates
        `(("n" "note" plain
           ,(format "#+title: ${title}\n%%[%s/template/note.org]" org-roam-directory)
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

;;; DASHBOARD CUSTOMIZATION
(remove-hook '+doom-dashboard-functions #'doom-dashboard-widget-shortmenu)
(remove-hook '+doom-dashboard-functions #'doom-dashboard-widget-footer)


(defun my-weebery-is-always-greater ()
  (let* ((banner '("KKKKKKKKK    KKKKKKKRRRRRRRRRRRRRRRRR   77777777777777777777XXXXXXX       XXXXXXX"
                   "K:::::::K    K:::::KR::::::::::::::::R  7::::::::::::::::::7X:::::X       X:::::X"
                   "K:::::::K    K:::::KR::::::RRRRRR:::::R 7::::::::::::::::::7X:::::X       X:::::X"
                   "K:::::::K   K::::::KRR:::::R     R:::::R777777777777:::::::7X::::::X     X::::::X"
                   "KK::::::K  K:::::KKK  R::::R     R:::::R           7::::::7 XXX:::::X   X:::::XXX"
                   "  K:::::K K:::::K     R::::R     R:::::R          7::::::7     X:::::X X:::::X   "
                   "  K::::::K:::::K      R::::RRRRRR:::::R          7::::::7       X:::::X:::::X    "
                   "  K:::::::::::K       R:::::::::::::RR          7::::::7         X:::::::::X     "
                   "  K:::::::::::K       R::::RRRRRR:::::R        7::::::7          X:::::::::X     "
                   "  K::::::K:::::K      R::::R     R:::::R      7::::::7          X:::::X:::::X    "
                   "  K:::::K K:::::K     R::::R     R:::::R     7::::::7          X:::::X X:::::X   "
                   "KK::::::K  K:::::KKK  R::::R     R:::::R    7::::::7        XXX:::::X   X:::::XXX"
                   "K:::::::K   K::::::KRR:::::R     R:::::R   7::::::7         X::::::X     X::::::X"
                   "K:::::::K    K:::::KR::::::R     R:::::R  7::::::7          X:::::X       X:::::X"
                   "K:::::::K    K:::::KR::::::R     R:::::R 7::::::7           X:::::X       X:::::X"
                   "KKKKKKKKK    KKKKKKKRRRRRRRR     RRRRRRR77777777            XXXXXXX       XXXXXXX"
                  ))
         (longest-line (apply #'max (mapcar #'length banner))))
    (put-text-property
     (point)
     (dolist (line banner (point))
       (insert (+doom-dashboard--center
                +doom-dashboard--width
                (concat line (make-string (max 0 (- longest-line (length line))) 32)))
               "\n"))
     'face 'doom-dashboard-banner)))

(setq +doom-dashboard-ascii-banner-fn #'my-weebery-is-always-greater)
(add-hook! '+doom-dashboard-functions :append
  (insert "\n" (+doom-dashboard--center +doom-dashboard--width "Pressure is a Privilege")))

(defvar activity-trap-file-path "~/.activity-trap")

(defun activity-trap (description)
  (interactive "s")
  (with-temp-buffer
    (insert description)
    (write-file activity-trap-file-path)))

(global-set-key (kbd "C-c C-p") 'activity-trap)

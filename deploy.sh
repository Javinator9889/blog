#!/bin/bash

# Exit on error
set -e

if [ -f .env ];
then
    source ./.env
fi

# Check if remote directory is set
if [ -z "$BLOG_DIR" ];
then
    echo "Remote directory is not set. Please, update \$BLOG_DIR"
    exit 1
fi

# Adjust permissions
echo "Setting directory permissions to 0770 (rwx rwx ---)"
find blogserver/ -type d -exec chmod 0770 {} \;

echo "Setting file permissions to 0660 (rw- rw- ---)"
find blogserver/ -type f -exec chmod 0660 {} \;

echo "Syncing files..."
rsync -avh --exclude='.DS_Store' --delete blogserver/ ${BLOG_DIR}

echo "Removing blogserver directory..."
rm -rv blogserver/

exit 0